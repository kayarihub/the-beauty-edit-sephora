"""Historical Sephora Kaggle product and review analytics. Python standard library."""
from pathlib import Path
from collections import defaultdict
import csv,json,sqlite3,math,statistics
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'data'/'raw'; OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
if not (RAW/'product_info.csv').exists() or not list(RAW.glob('reviews_*.csv')):
    raise SystemExit('Download product_info.csv and reviews_*.csv from Kaggle into data/raw/.')
def num(v):
    try:
        x=float(v)
        return x if math.isfinite(x) else None
    except (ValueError,TypeError): return None
products={}
with (RAW/'product_info.csv').open(encoding='utf-8-sig',newline='') as f:
    for r in csv.DictReader(f):
        pid=(r.get('product_id') or '').strip()
        if pid:
            products[pid]={'id':pid,'name':r.get('product_name') or 'Unnamed','brand':r.get('brand_name') or 'Unknown','category':r.get('primary_category') or 'Other','price':num(r.get('price_usd')),'rating':num(r.get('rating')),'loves':num(r.get('loves_count')) or 0,'review_count_dataset':0,'review_avg_dataset':None}
stats=defaultdict(lambda:[0,0,0])
total=matched=0
for path in sorted(RAW.glob('reviews_*.csv')):
    with path.open(encoding='utf-8-sig',newline='') as f:
        for r in csv.DictReader(f):
            total+=1;pid=r.get('product_id')
            if pid not in products:continue
            matched+=1;s=stats[pid];s[0]+=1
            rating=num(r.get('rating'))
            if rating is not None and 1<=rating<=5:s[1]+=rating;s[2]+=1
for pid,p in products.items():
    n,sm,valid=stats[pid];p['review_count_dataset']=n;p['review_avg_dataset']=round(sm/valid,3) if valid else None
rows=list(products.values());prices=[p['price'] for p in rows if p['price'] is not None]
summary={'product_count':len(rows),'brand_count':len({p['brand'] for p in rows}),'review_rows':total,'matched_review_rows':matched,'average_list_price':round(statistics.mean(prices),2) if prices else None,'source':'Kaggle nadyinky historical Sephora dataset'}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
with (OUT/'product_metrics.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]) if rows else ['id']);writer.writeheader();writer.writerows(rows)
db=sqlite3.connect(OUT/'sephora_analytics.sqlite')
db.execute('DROP TABLE IF EXISTS products')
db.execute('CREATE TABLE products(product_id TEXT PRIMARY KEY,product_name TEXT,brand_name TEXT,category TEXT,price_usd REAL,rating REAL,loves_count REAL,review_count_dataset INTEGER,review_avg_dataset REAL)')
db.executemany('INSERT INTO products VALUES(?,?,?,?,?,?,?,?,?)',[(p['id'],p['name'],p['brand'],p['category'],p['price'],p['rating'],p['loves'],p['review_count_dataset'],p['review_avg_dataset']) for p in rows]);db.commit();db.close()
template=(ROOT/'dashboard'/'template.html').read_text(encoding='utf-8')
payload=json.dumps({'summary':summary,'products':rows},ensure_ascii=True).replace('</','<\\/')
(ROOT/'dashboard'/'index.html').write_text(template.replace('/*__DATA__*/',payload),encoding='utf-8')
print('Built dashboard from',len(rows),'products and',total,'review records; matched',matched)
