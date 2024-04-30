from collections import defaultdict

# Initialize state
timezone_offset = 0
audits = {}
proves = {}
allSummedPlotting = 0
allSummedplottingCount = 0
avgtime = defaultdict(lambda: {})
balance = "0.0"
best_block = str()
connected_farmer = False
curr_farm_name = "Default"
curr_farm = None
curr_line = str()
curr_sector_disk = defaultdict(lambda: 0)
deltas = defaultdict(lambda: '00:00')
disk_farms = set()
dl = str()
drive_directory = {}
errors = [str(), str(), str(), str(), str(), str(), str(),]
#event_times = defaultdict(int)
#farm_deltas = defaultdict(lambda: {})
farmer_data = {}
farmer_ip = "127.0.0.1"
farmer_name = 'WolfrageRocks'  # str()
farmer_port = 8016
farm_id_mapping = {}
farm_metrics = {}
farm_names = []
farm_plot_size = defaultdict(lambda: "0")
farm_recent_rewards = defaultdict(lambda: int)
farm_recent_skips = defaultdict(int)
farm_rewards = defaultdict(lambda: int)
farm_reward_times = defaultdict(lambda: [])
farm_skips = defaultdict(int)
farm_skip_times = defaultdict(lambda: [])
finalized = str()
frame_delays = -1
front_end_ip = "127.0.0.1"
front_end_port = 8181
hour_24 = False
imported = str()
l3_concurrency = 1
l3_farm_sector_time = 0
l3_timestamps = []
last_farm = int()
last_logs = [str(), str(), str(), str(), str(), str(), str(),]
# However many initialized is how many it'll show
last_node_logs = [str(), str(), str(), str(), str(), str(),]
#last_sector_time = defaultdict(lambda: int)
latest_version = "Unknown"
layout = None
live_drives = []
max_index = 0
name = str()
node_errors = [str(), str(), str(), str(), str(), str(), str(),]
node_log_file = str()
node_warnings = [str(), str(), str(), str(), str(), str(), str(),]
no_more_drives = False
peers = str()
plot_space = {}
plot_time_seconds = 0.0
prove_method = defaultdict(lambda: {})
psdTotal = 0
psTotal = 0
remote_farms = {}
remTotal = 0
# replotting = defaultdict(lambda: False)
reward_count = 0
rewards_per_hr = defaultdict(lambda: [])
running = False
sectime = {}
sector_times = defaultdict(lambda: 0)
show_logging = True
startTime = 0
system_stats = {}
tib_hr = 0
toggle_encoding = False
toggle_encoding_node = False
total_completed = 0
total_error_count = 0
ui_port = '8016'
ul = str()
unroll = False
wallet = str()
warnings = [str(), str(), str(), str(), str(), str(), str(),]

