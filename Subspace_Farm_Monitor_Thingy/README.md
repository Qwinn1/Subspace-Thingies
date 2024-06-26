# Subspace-Thingies

## Farm Monitor Thingy

![image](https://github.com/wolfrage76/Subspace-Thingies/assets/75458290/d0b172b6-6041-48ae-949b-22727d5f7dd9)

- Multiple languages supported! (en, cn, uk, vi, es, fr, jp  and others!)
- Remote farmers
- Stale farmer alerts
- Monitors your wallet for balance changes
- Lots more!

Ping me on the Subspace Discord (Wolfrage) if you have any questions. No DMs though -- DMs are the Devil's handjob.

Installation: (Chinese guide available HERE: https://forum.subspace.network/t/node-farm-ubuntu/3190)
 - You must add `--rpc-listen-on <LocalIP>:<Port>` to your NODE launch command - port 9944 is default
 - You must add `--prometheus-listen-on <localIP>:<Port>` to your FARMER launch command - port 8181 is default
 - If you need to create a farmer log file, add this to the end of your launch command: ` |tee -a <FILENAME>.txt`


FOR BOTH SIDES:
1. Edit `config.yaml.example` and save it as `config.yaml` 
2. Copy `config.yaml` to both monitor and viewer folders
3. Run: `pip install -r requirements.txt`


THEN FOR FARMER SIDE:
1. Save monitor folder to the farmer
3. Run: `monitor.py` to launch


THEN FOR VIEWER:
1. Copy the Viewer folder to a machine you can connect to the console for
2. In the folder Run: `pip install -r requirements.txt`
3. Run: `python view.py` to launch

The UI will not fully update until a machine cycles and sends its data over.  If the drive list is empty after awhile, or if you get Unicode Errors, edit config.yaml and toggle the "TOGGLE_ENCODING" setting.

