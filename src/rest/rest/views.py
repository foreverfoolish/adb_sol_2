from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from pymongo import MongoClient

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']
collection1 = db["todolist"]
class TodoListView(APIView):

    def get(self, request):
        # Implement this method - return all todo items from db instance above.
        result=[]
        todo = collection1.find({})
        for r in todo:
            #result.append("name:\x7f\x7f")
            result.append(r["name"])
        resp={"task_list":result}
        return Response(resp, status=status.HTTP_200_OK)
        
    def post(self, request):
        # Implement this method - accept a todo item in a mongo collection, persist it using db instance above.
        collection1.insert(request.data)
        return Response(request.data, status=status.HTTP_200_OK)

