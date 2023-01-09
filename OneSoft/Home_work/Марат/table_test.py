from prettytable import PrettyTable

x = PrettyTable()

x.field_names = ["a", "b"]
x.add_row([1, "asdf"])
print(x)


a, b;
1, asdf