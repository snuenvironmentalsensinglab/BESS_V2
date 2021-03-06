import json
from landsatxplore.api import API
from landsatxplore.earthexplorer import EarthExplorer

username="henockmao54@snu.ac.kr"
password="jh|WMe3A9DAK44n"

api = API("henockmao54@snu.ac.kr","jh|WMe3A9DAK44n")

scenes = api.search(
    dataset='landsat_ot_c2_l2',
    bbox= (127.21710138948873,38.18195837298332,127.27222505323994,38.22346787684907),    
    start_date='2019-08-01',
    end_date='2019-12-01'  
)

print(f"{len(scenes)} scenes found.")

print(scenes[0]["landsat_scene_id"])

ee = EarthExplorer(username, password)

for s in scenes:
    print(s["display_id"])
    ee.download(scenes[0]["landsat_scene_id"], output_dir='data/')
 