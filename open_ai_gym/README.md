# Open_Ai_Gym
open_ai_gymについてまとめる
## 警告について
```
WARN: gym.spaces.Box autodetected dtype as <class 'numpy.float32'>. Please provide explicit dtype.
```
上記のような警告がでる場合  
1. ``` pip show gym``` を実行しgymのインストールディレクトリへ移動
2. ``` gym/spaces/box.py``` をエディタで開く
3. 開いたファイルの``` __init__``` の``` dtype=None``` を ```dtype=np.float32``` に変更する
