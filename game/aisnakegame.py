from snake.game import Game,GameConf,GameMode

greedy="GreedySolver"
hamilton="HamiltonSolver"

normal=GameMode.NORMAL

conf=GameConf()
conf.solver_name=greedy
conf.mode=normal
print("SOLVER:  ",(conf.solver_name))

print("MODE:  ",(conf.mode))
Game(conf).run()
