main=input("Enter main string: ")
prefix=input("Enter prefix: ")
suffix=input("Enter suffix: ")

l1=main.startswith(prefix)
l2=main.endswith(suffix)

if l1:
    print("starts with prefix")

else:
    print("doesn't start with prefix")


if l2:
    print("ends with suffix")

else:
    print("doesn't end with suffix")