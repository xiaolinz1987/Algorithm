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

    def mining_v2(self):
        result_table = [[0 for i in range(self.workers+1)] for i in range(len(self.mining_amount)+1)]

        for i in range(1, len(self.mining_amount)+1):
            for j in range(1, self.workers+1):
                if j < self.mining_workers[i-1]:
                    result_table[i][j] = result_table[i-1][j]
                else:
                    result_table[i][j] = max(result_table[i-1][j], 
                            result_table[i-1][j-self.mining_workers[i-1]] + self.mining_amount[i-1])

        self.result = result_table[len(self.mining_amount)][workers]

    def mining_v3(self):
        result_table = [0] * (self.workers+1)
        
        for i in range(1, len(self.mining_amount)+1):
            for j in range(self.workers, 0, -1):
                if j >= self.mining_workers[i-1]:
                    result_table[j] = max(result_table[j], 
                            result_table[j-self.mining_workers[i-1]] + self.mining_amount[i-1])

        self.result = result_table[self.workers]

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
mining.reset(workers, mines, mining_workers, mining_amount)
mining.mining_v2()
print("mining_v2:")
mining.output()
mining.reset(workers, mines, mining_workers, mining_amount)
mining.mining_v3()
print("mining_v3:")
mining.output()

