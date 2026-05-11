# 10. Write a Python program to perform set operations such as
# union, intersection, and difference on student roll numbers.

print("*" * 40)
print("      SET OPERATIONS")
print("*" * 40)

set1 = set(map(int, input("\nEnter elements of Set 1: ").split()))

set2 = set(map(int, input("Enter elements of Set 2: ").split()))

print("\nUnion :", set1 | set2)

print("Intersection :", set1 & set2)

print("Difference (Set1 - Set2) :", set1 - set2)