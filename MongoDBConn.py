{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pymongo import MongoClient"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "client = MongoClient() # 클래스 객체 할당 \n",
    "client = MongoClient('localhost', 27017)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "db = client[\"test\"] #db이름\n",
    "collection = db[\"employees\"] # db.employees // collection = db.coll_이름\n",
    "print(collection)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "coll_list = db.collection_names() #컬렉션의 리스트 보기\n",
    "print(coll_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "emp = collection.find_one()\n",
    "emp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "emp_list = collection.find()\n",
    "for emp in emp_list:\n",
    "    print(emp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "client = MongoClient('localhost', 27017)\n",
    "db = client.test\n",
    "col = db.person\n",
    "\n",
    "p = {'name' : '한석희', 'age' : 50, 'gender' : '남'}\n",
    "p_list = [\n",
    "    {'name' : '강나래', 'age' : 23, 'gender' : '여'},\n",
    "    {'name' : '이하윤', 'age' : 25, 'gender' : '남'},\n",
    "    {'name' : '고명수', 'age' : 30, 'gender' : '남'},\n",
    "    {'name' : '이만세', 'age' : 30, 'gender' : '남'},\n",
    "    {'name' : '김림용', 'age' : 30, 'gender' : '남'}\n",
    "]\n",
    "#col.insert_one(p) # insert(p)\n",
    "#col.insert_many(p_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#for person in col.find({'gender' : '여'}, {'_id' : 0}):\n",
    "for person in col.find({},{'_id' : 0}):\n",
    "    print(person)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#col.remove({'name' : '김림용'})\n",
    "#p2 = {'name' : '고명수', 'age' : 50, 'gender' : '여'}\n",
    "col.update_many({'name' : '이만세'}, {'$set' : {'sal' : 300}})\n",
    "#col.update_one({'name' : '고명수'}, {'$set' : {'age' : 50, 'gender' : '여'}})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pymongo.results.InsertManyResult at 0x27889f1a380>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "client = MongoClient('localhost', 27017)\n",
    "db = client.test\n",
    "col = db.member\n",
    "\n",
    "member_list = [\n",
    "    {'id' : 'abcd', 'pw' : 1234, 'name' : '홍길동', 'point' : 10},\n",
    "    {'id' : 'aaaa', 'pw' : 'aaaa', 'name' : '한재현', 'point' : 20},\n",
    "    {'id' : 'bbbb', 'pw' : 'bbbb', 'name' : '고명수', 'point' : 15},\n",
    "    {'id' : 'cccc', 'pw' : 'cccc', 'name' : '이하윤', 'point' : 10}\n",
    "]\n",
    "col.insert_many(member_list)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': ObjectId('5fb73308bd094a54d31ac2ba'), 'id': 'abcd', 'pw': 1234, 'name': '홍길동', 'point': 15, 'gift': 'Y'}\n",
      "{'_id': ObjectId('5fb73308bd094a54d31ac2bb'), 'id': 'aaaa', 'pw': 'aaaa', 'name': '한재현', 'point': 20, 'gift': 'Y'}\n",
      "{'_id': ObjectId('5fb73308bd094a54d31ac2bc'), 'id': 'bbbb', 'pw': 'bbbb', 'name': '고명수', 'point': 15, 'gift': 'Y'}\n"
     ]
    }
   ],
   "source": [
    "# 1. 전체 데이터 가져오기\n",
    "for member in col.find():\n",
    "    print(member)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': ObjectId('5fb73308bd094a54d31ac2ba'), 'id': 'abcd', 'pw': 1234, 'name': '홍길동', 'point': 15}\n",
      "{'_id': ObjectId('5fb73308bd094a54d31ac2bb'), 'id': 'aaaa', 'pw': 'aaaa', 'name': '한재현', 'point': 20, 'gift': 'Y'}\n",
      "{'_id': ObjectId('5fb73308bd094a54d31ac2bc'), 'id': 'bbbb', 'pw': 'bbbb', 'name': '고명수', 'point': 15}\n"
     ]
    }
   ],
   "source": [
    "# 2. point가 15이상인 것 가져오기\n",
    "for member in col.find({'point' : {'$gte' : 15}}):\n",
    "    print(member)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pymongo.results.UpdateResult at 0x27889e1a740>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 3. 홍길동의 point를 15로 수정\n",
    "col.update_one({'name' : '홍길동'}, {'$set' : {'point' : 15}})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pymongo.results.UpdateResult at 0x27889f0dac0>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4. point가 15이상인 데이터에 gift 필드를 추가하고 'Y' 값을 추가한다.\n",
    "col.update_many({'point' : {'$gte' : 15}}, {'$set' : {'gift' : 'Y'}})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pymongo.results.DeleteResult at 0x27889f07dc0>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 5. id가 cccc인 데이터를 삭제한다.\n",
    "col.delete_many({'id' : 'cccc'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
