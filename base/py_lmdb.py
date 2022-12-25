from encodings.utf_8 import decode
import lmdb


def lmdb_crud():
    # 如果文件夹下没有data.mbd或lock.mdb文件，则会生成一个空的，如果有，不会覆盖
    # map_size定义最大储存容量，单位是byte，以下定义1GB容量
    env = lmdb.open('base', map_size=1024**3)

    txn = env.begin(write=True)

    # 添加数据和键值
    txn.put(key='1'.encode('utf-8'), value='aaa'.encode('utf-8'))
    txn.put(key='2'.encode('utf-8'), value='bbb'.encode('utf-8'))
    txn.put(key='3'.encode('utf-8'), value='ccc'.encode('utf-8'))

    # 通过键值删除数据
    txn.delete(key='1'.encode('utf-8'))

    # 修改数据
    txn.put(key='3'.encode('utf-8'), value='ddd'.encode('utf-8'))

    # 通过commit()函数提交更改
    txn.commit()

    env.close()

#----------------------------------------------------------------------------

def  lmdb_query():
    env = lmdb.open("base")
    # 参数write设置为True才可以写入
    txn = env.begin(write=True)
    ############################################添加、修改、删除数据

    # 添加数据和键值
    txn.put(key='6'.encode('utf-8'), value='eee'.encode('utf-8'))
    txn.put(key='7'.encode('utf-8'), value='你好'.encode('utf-8'))

    # 通过键值删除数据
    txn.delete(key='2'.encode('utf-8'))

    # 修改数据
    txn.put(key='3'.encode('utf-8'), value='qqq'.encode('utf-8'))

    # 通过commit()函数提交更改
    txn.commit()
    ############################################查询lmdb数据
    txn = env.begin()

    # get函数通过键值查询数据
    print(txn.get(str(7).encode('utf-8')))

    # 通过cursor()遍历所有数据和键值
    for key, value in txn.cursor():
        print(key, decode(value)[0])

#----------------------------------------------------------------------------

if __name__ == '__main__':
    lmdb_query()
