#open_ai_gym動作確認用
import gym
import time
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    a = env.step(env.action_space.sample())
    #指定角度より倒れるとTrueが帰ってくる=>環境をリセットする(警告回避)
    if a[2] == True:
        env.reset()
    #time.sleepがないと早すぎ
    time.sleep(0.02)
env.close()

