import itertools

# class X():
#     def who_am_i(self):
#         print("I am a X")


# class Y():
#     def who_am_i(self):
#         print("I am a Y")


# class A(X, Y):
#     def who_am_i(self):
#         print("I am a A")


# class B(Y, X):
#     def who_am_i(self):
#         print("I am a B")


# class F(A, B):
#     def who_am_i(self):
#         print("I am a F")

class A():
    pass

class B(A):
    pass

# MRO=[C, [B, A, obj], [A, obj]]
class C(B, A): # C(A, B)不符合MRO一致性原则
    pass

# MRO Method Resolution Order
def C3(cls, *mro_lists):
    # copy一份，不影响传入的参数
    mro_lists = [list(mro_list[:]) for mro_list in mro_lists]

    # new mro list 
    mro = [cls]

    while True:
        candidate_found = False

        for mro_list in mro_lists:
            if not len(mro_list):
                continue # 跳过空列表

            candidate = mro_list[0]

            if candidate_found:
                if candidate in mro: # 如果当前MRO列表第一个元素是上一轮被找到的candidate，就将其删除
                    mro_list.pop(0) 
                continue # 这一轮选出candidate后，就不用再测试了

            # 如果候选在后续 MRO 的中间还有出现，为了 MRO 的一致性，就不能选其candidate
            # MRO 的一致性: 每个类的 MRO 在最终的 MRO 中必须不能改变
            if candidate in itertools.chain(*(x[1:] for x in mro_lists)):
                continue
            else:
                mro.append(candidate)
                mro_list.pop(0)
                candidate_found = True 
            
        if not sum(len(mro_list) for mro_list in mro_lists):
            # mor_lists 空了，说明已经完全处理完了
            break

        if not candidate_found: # 如果一轮下来没找到candidate，说明类声明顺序有问题，会造成MRO不一致
            raise TypeError("Inconsistent MRO")

    return mro


print(C3('C', ['A', 'object'], ['B', 'A', 'object']))


# def mro(cls):
#     if cls is object:
#         return [object]
#     return [cls] + merge([mro(base) for base in cls.__bases__])

# def merge(mros):
#     if not any(mros):  # all lists are empty
#         return []  # base case
#     for candidate, *_ in mros:
#         if all(candidate not in tail for _, *tail in mros):
#             return [candidate] + merge([tail if head is candidate else [head, *tail]
#                                         for head, *tail in mros])
#     else:
#         raise TypeError("No legal mro")
