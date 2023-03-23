# import csv
# with open('C:\Semestr 4\Mownit\Zestaw 0\dat.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         i=0
#         if row:
#             x.append(float(row[0]))
#             y.append(i)
#             i+=1
#
# fig, ax = plt.subplots()
# ax.plot(x, y)
#
# # Zmiana precyzji osi y
# ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))
#
# # Wyświetlenie wykresu
# plt.show()

# df = pd.read_csv('C:\Semestr 4\Mownit\Zestaw 0\dat.csv', header=None)
# data = df.values.tolist()
# def search(data):
#     sol = []
#     for d in range(1):
#         y = data[d]
#         for i in range(len(y)):
#             y[i] = round(y[i],2)
#         for i in range(len(y)-2):
#             if (y[i],y[i+1],y[i+2])==(y[0],y[1],y[2]):
#                 sol.append(i)
#     return data[0][246:311]
# print(search(data))

if __name__ == '__main__':
    import pandas as pd
    import matplotlib.pyplot as plt

    # wczytanie danych z pliku csv
    df = pd.read_csv('C:\Semestr 4\Mownit\Zestaw 0\dat.csv', header=None)

    # przekształcenie dataframe do listy
    data = df.values.tolist()

    # przetworzenie danych
    y = [row[3] for row in data]
    y = y[1:3]+y[4:6]
    print(y)
    # x = ["float","double","long double","floatp","doublep","long dooublep"]
    x = [ "double", "long double","doublep", "long dooublep"]

    # rysowanie wykresów
    plt.xlabel('Typ zmiennej')
    plt.ylabel('wartość elementu')
    plt.ylim(min(y), max(y))
    plt.scatter(x, y)
    plt.show()


