class MyBestGoldMining:

    def __init__(self, workers, mines, mining_workers, mining_amount):
        self.workers = workers
        self.mines = mines
        self.mining_workers = mining_workers
        self.mining_amount = mining_amount
        self.result = 0

    def reset(self, workers, mines, mining_workers, mining_amount):
        self.workers = workers
        self.mines = mines
        self.mining_workers = mining_workers
        self.mining_amount = mining_amount
        self.result = 0

    def __mining_v1_core(self, workers, mines, mining_workers, mining_amount):
        if workers == 0 or mines == 0:
            return 0
        if workers < mining_workers[mines - 1]:
            return self.__mining_v1_core(workers, mines - 1, mining_workers, mining_amount)
        return max(self.__mining_v1_core(workers, mines - 1, mining_workers, mining_amount),
                self.__mining_v1_core(workers - mining_workers[mines - 1], mines - 1, mining_workers, mining_amount) + mining_amount[mines - 1])

    def mining_v1(self):
        self.result = self.__mining_v1_core(self.workers, self.mines, self.mining_workers, self.mining_amount)

    def output(self):
        print(self.result)

workers = 10
mines = 5
mining_workers = list([5, 5, 3, 4, 3])
mining_amount = list([400, 500, 200, 300, 350])
mining = MyBestGoldMining(workers, mines, mining_workers, mining_amount)
mining.mining_v1()
print("mining_v1:")
mining.output()

