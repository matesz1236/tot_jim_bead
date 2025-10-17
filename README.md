## A csomag klónozása

```bash
cd ~/ros2_ws/src
git clone https://github.com/matesz1236/tot_jim_bead.git
```

## Csomag buildelése
```bash
cd ~/ros2_ws
colcon build --packages-select random_stats_pkg --symlink-install
```
## Környezet betöltése 
```bash
source ~/ros2_ws/install/setup.bash
```

## Csomag futtatása
# 1. lehetőség — launch fájllal (ajánlott)

Ez a parancs egyszerre elindítja mindkét node-ot:
```bash
ros2 launch random_stats_pkg random_stats_launch.py
```
# 2. lehetőség — külön terminálokban

Terminál 1:
```bash
ros2 run random_stats_pkg random_publisher
```
Terminál 2:
```bash
ros2 run random_stats_pkg stats_node
```
## Graph

![RQT Graph](rosgraph.png)
