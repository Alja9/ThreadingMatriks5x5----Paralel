import threading
import time

# Matriks 5x5
matrix_a = [[10250,12399,23456,50560,21234],[40333,87777,32323,22222,50444],[70700,80000,90999,22229,32341],[51323,34567,99992,12233,22339],[41123,42222,43329,44111,45101]]
matrix_b = [[53,54,55,56,57],[68,67,66,65,64],[71,73,75,77,79],[80,85,82,84,88],[95,96,97,98,99]]

# Hasil
matrix_c = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

class Thread1(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print("Starting " + self.name + "\n")

        vector_a1 = matrix_a[0]
        matrix_c[0][0] = vector_a1[0] * matrix_b[0][0] + vector_a1[1] * matrix_b[1][0] + vector_a1[2] * matrix_b[2][0] + vector_a1[3] * matrix_b[3][0] + vector_a1[4] * matrix_b[4][0]
        matrix_c[0][1] = vector_a1[0] * matrix_b[0][1] + vector_a1[1] * matrix_b[1][1] + vector_a1[2] * matrix_b[2][1] + vector_a1[3] * matrix_b[3][1] + vector_a1[4] * matrix_b[4][1]
        matrix_c[0][2] = vector_a1[0] * matrix_b[0][2] + vector_a1[1] * matrix_b[1][2] + vector_a1[2] * matrix_b[2][2] + vector_a1[3] * matrix_b[3][2] + vector_a1[4] * matrix_b[4][2]
        matrix_c[0][3] = vector_a1[0] * matrix_b[0][3] + vector_a1[1] * matrix_b[1][3] + vector_a1[2] * matrix_b[2][3] + vector_a1[3] * matrix_b[3][3] + vector_a1[4] * matrix_b[4][3]
        matrix_c[0][4] = vector_a1[0] * matrix_b[0][4] + vector_a1[1] * matrix_b[1][4] + vector_a1[2] * matrix_b[2][4] + vector_a1[3] * matrix_b[3][4] + vector_a1[4] * matrix_b[4][4]

        print("End " + self.name + "\n")


class Thread2(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print("Starting " + self.name + "\n")

        vector_a2 = matrix_a[1]
        matrix_c[1][0] = vector_a2[0] * matrix_b[0][0] + vector_a2[1] * matrix_b[1][0] + vector_a2[2] * matrix_b[2][0] + vector_a2[3] * matrix_b[3][0] + vector_a2[4] * matrix_b[4][0]
        matrix_c[1][1] = vector_a2[0] * matrix_b[0][1] + vector_a2[1] * matrix_b[1][1] + vector_a2[2] * matrix_b[2][1] + vector_a2[3] * matrix_b[3][1] + vector_a2[4] * matrix_b[4][1]
        matrix_c[1][2] = vector_a2[0] * matrix_b[0][2] + vector_a2[1] * matrix_b[1][2] + vector_a2[2] * matrix_b[2][2] + vector_a2[3] * matrix_b[3][2] + vector_a2[4] * matrix_b[4][2]
        matrix_c[1][3] = vector_a2[0] * matrix_b[0][3] + vector_a2[1] * matrix_b[1][3] + vector_a2[2] * matrix_b[2][3] + vector_a2[3] * matrix_b[3][3] + vector_a2[4] * matrix_b[4][3]
        matrix_c[1][4] = vector_a2[0] * matrix_b[0][4] + vector_a2[1] * matrix_b[1][4] + vector_a2[2] * matrix_b[2][4] + vector_a2[3] * matrix_b[3][4] + vector_a2[4] * matrix_b[4][4]

        print("End " + self.name + "\n")

class Thread3(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print("Starting " + self.name + "\n")

        vector_a3 = matrix_a[2]
        matrix_c[2][0] = vector_a3[0] * matrix_b[0][0] + vector_a3[1] * matrix_b[1][0] + vector_a3[2] * matrix_b[2][0] + vector_a3[3] * matrix_b[3][0] + vector_a3[4] * matrix_b[4][0]
        matrix_c[2][1] = vector_a3[0] * matrix_b[0][1] + vector_a3[1] * matrix_b[1][1] + vector_a3[2] * matrix_b[2][1] + vector_a3[3] * matrix_b[3][1] + vector_a3[4] * matrix_b[4][1]
        matrix_c[2][2] = vector_a3[0] * matrix_b[0][2] + vector_a3[1] * matrix_b[1][2] + vector_a3[2] * matrix_b[2][2] + vector_a3[3] * matrix_b[3][2] + vector_a3[4] * matrix_b[4][2]
        matrix_c[2][3] = vector_a3[0] * matrix_b[0][3] + vector_a3[1] * matrix_b[1][3] + vector_a3[2] * matrix_b[2][3] + vector_a3[3] * matrix_b[3][3] + vector_a3[4] * matrix_b[4][3]
        matrix_c[2][4] = vector_a3[0] * matrix_b[0][4] + vector_a3[1] * matrix_b[1][4] + vector_a3[2] * matrix_b[2][4] + vector_a3[3] * matrix_b[3][4] + vector_a3[4] * matrix_b[4][4]

        print("End " + self.name + "\n")

class Thread4(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print("Starting " + self.name + "\n")

        vector_a4 = matrix_a[3]
        matrix_c[3][0] = vector_a4[0] * matrix_b[0][0] + vector_a4[1] * matrix_b[1][0] + vector_a4[2] * matrix_b[2][0] + vector_a4[3] * matrix_b[3][0] + vector_a4[4] * matrix_b[4][0]        
        matrix_c[3][1] = vector_a4[0] * matrix_b[0][1] + vector_a4[1] * matrix_b[1][1] + vector_a4[2] * matrix_b[2][1] + vector_a4[3] * matrix_b[3][1] + vector_a4[4] * matrix_b[4][1]
        matrix_c[3][2] = vector_a4[0] * matrix_b[0][2] + vector_a4[1] * matrix_b[1][2] + vector_a4[2] * matrix_b[2][2] + vector_a4[3] * matrix_b[3][2] + vector_a4[4] * matrix_b[4][2]
        matrix_c[3][3] = vector_a4[0] * matrix_b[0][3] + vector_a4[1] * matrix_b[1][3] + vector_a4[2] * matrix_b[2][3] + vector_a4[3] * matrix_b[3][3] + vector_a4[4] * matrix_b[4][3]
        matrix_c[3][4] = vector_a4[0] * matrix_b[0][4] + vector_a4[1] * matrix_b[1][4] + vector_a4[2] * matrix_b[2][4] + vector_a4[3] * matrix_b[3][4] + vector_a4[4] * matrix_b[4][4]

        print("End " + self.name + "\n")

class Thread5(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print("Starting " + self.name + "\n")

        vector_a5 = matrix_a[4]
        matrix_c[4][0] = vector_a5[0] * matrix_b[0][0] + vector_a5[1] * matrix_b[1][0] + vector_a5[2] * matrix_b[2][0] + vector_a5[3] * matrix_b[3][0] + vector_a5[4] * matrix_b[4][0]
        matrix_c[4][1] = vector_a5[0] * matrix_b[0][1] + vector_a5[1] * matrix_b[1][1] + vector_a5[2] * matrix_b[2][1] + vector_a5[3] * matrix_b[3][1] + vector_a5[4] * matrix_b[4][1]
        matrix_c[4][2] = vector_a5[0] * matrix_b[0][2] + vector_a5[1] * matrix_b[1][2] + vector_a5[2] * matrix_b[2][2] + vector_a5[3] * matrix_b[3][2] + vector_a5[4] * matrix_b[4][2]
        matrix_c[4][3] = vector_a5[0] * matrix_b[0][3] + vector_a5[1] * matrix_b[1][3] + vector_a5[2] * matrix_b[2][3] + vector_a5[3] * matrix_b[3][3] + vector_a5[4] * matrix_b[4][3]
        matrix_c[4][4] = vector_a5[0] * matrix_b[0][4] + vector_a5[1] * matrix_b[1][4] + vector_a5[2] * matrix_b[2][4] + vector_a5[3] * matrix_b[3][4] + vector_a5[4] * matrix_b[4][4]

        print("End " + self.name + "\n")        

if __name__ == '__main__':
    start = int(round(time.time() * 1000))
    thread1 = Thread1(1,"Thread 1")
    thread2 = Thread2(2,"Thread 2")
    thread3 = Thread3(3,"Thread 3")
    thread4 = Thread4(4,"Thread 4")
    thread5 = Thread5(5,"Thread 5")

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    print("Execution Time --->", (int(round(time.time() * 1000)) - start))
    for x in matrix_c:
        print(x)
