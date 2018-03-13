# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

import json

# Create your views here.

class TestView(APIView):

    def get(self, request):
        with open("/Users/kevindenny/Documents/automated-reports/dj_app/bq_api/content_data.json", 'r') as gf:
            hg = json.load(gf)

            md = {'data': hg}
            return Response(md)

class TestPost(APIView):

    def post(self, request):
        datum = str(request.data['string'])

        a = {'data': datum}

        return Response(a)