"""
The good old SGD code
usage: python SGD.py train.csv WC_traffictype test.csv submit.csv
"""

#!/usr/env/python
import hashlib
import math
from math import log, exp, sqrt

import sys

import scipy as sp
def llfun(act, pred):
    try:
        epsilon = 1e-15
        pred = sp.maximum(epsilon, pred)
        pred = sp.minimum(1-epsilon, pred)
        ll = sum(act*sp.log(pred) + sp.subtract(1,act)*sp.log(sp.subtract(1,pred)))
        ll = sum(ll)
        ll = ll * -1.0/len(act)
        return ll
    except:
        return 0

def O_ONE_LOSS(act, pred):
    epsilon = 1e-15
    pred = sp.maximum(epsilon, pred)
    pred = sp.minimum(1-epsilon, pred)
    ll = 0
    for i in range(0,len(act)):
        if (act[i][0] == 1 and pred[i][0] > 0.5) or (act[i][0] == 0 and pred[i][0] <= 0.5):
            ll = ll +1
    return float(ll)/float(len(act))

def getpos(string,arr):
    cnt = 0
    for a in arr:
        if string in a:
            return cnt
        else:
            cnt = cnt+1
    return cnt

trainfilename = sys.argv[1]
modeltype = sys.argv[2]

testfilename = sys.argv[3]
submitfilename = sys.argv[4]

pred = []
act = []

print "[INFO]processing the file: "+str(trainfilename)
print "[INFO]processing the model: "+str(modeltype)

def get_x(container):
    x = []
    x.append(0)
    for content in container:
        hash_out = int(hashlib.sha1(content).hexdigest(), 16) % (10 ** 4)
        x.append(hash_out)
    return x

def get_p(x):
    wtx = 0
    for i in x:
        wtx += w[i]
    #print "wtx: "+str(wtx)
    if wtx >= 20:
        wtx = 20
    if wtx <= -20:
        wtx = -20
    #print "probability: "+str(1./(1.+math.exp(-wtx)))
    return (1./(1.+math.exp(-wtx)))
def update_w(x,p,y):
    for i in x:
        n[i] += abs(p - y)
        w[i] -= (p - y) * 1. * alpha / sqrt(n[i])

"""
def update_w(x,p,y):
    for i in x:
        g = p-float(y)
        sigma  = (math.sqrt(uN[i] + g**2) - math.sqrt(uN[i]))/alpha
        z[i] += g + sigma * w[i]
        uN[i] += g**2
        if abs(z[i]) <= lambda_1:
            w[i] = 0
        else:
            w[i] = -(z[i] - sign(z[i]) * lambda_1) * ((lambda_2 + (beta + math.sqrt(uN[i]))/alpha)**-1)
        n[i] += 1
"""

def sign(x):
    if x > 0 or (x == 0 and (math.atan2(x, -1.) > 0.)):
        return 1
    else:
        return -1

D = 2**20

lambda_1 = 1
lambda_2 = 0.1

beta = 1
alpha = 0.1

w = [0]*D
n = [0]*D
z = [0]*D
uN = [0]*D
k = [0]*D

header = False
header_col = []

OW_Conjunctions = ["publisherid###appsitecategory","appsiteid###position","appsiteid###timestamp"]
WC_Conjunctions = ["publisherid###appsitecategory","appsiteid###position","appsiteid###timestamp","appsiteid###gender","appsiteid###country"]

allowed_cols_WC_traffictype = ["publisherid","appsiteid","appsitecategory","position","timestamp","gender","os","osvrsn","model","manufacturer","carrier","devicetype","deviceip","country","zipcode","geotype","campaignid","creativeid","Creativetype","creativecategory","outcome"]
allowed_cols_WC_appsiteid = ["traffictype","publisherid","appsitecategory","position","timestamp","gender","os","osvrsn","model","manufacturer","carrier","devicetype","deviceip","country","zipcode","geotype","campaignid","creativeid","Creativetype","creativecategory","outcome"]
allowed_cols_WC_appsitecategory = ["traffictype","publisherid","appsiteid","position","timestamp","gender","os","osvrsn","model","manufacturer","carrier","devicetype","deviceip","country","zipcode","geotype","campaignid","creativeid","Creativetype","creativecategory","exchangebid","outcome"]
allowed_cols_WC_campaignid = ["traffictype","publisherid","appsiteid","appsitecategory","position","timestamp","gender","os","osvrsn","model","manufacturer","carrier","devicetype","deviceip","country","zipcode","geotype","creativeid","Creativetype","creativecategory","outcome"]
allowed_cols_WC_publisherid = ["traffictype","appsiteid","appsitecategory","position","timestamp","gender","os","osvrsn","model","manufacturer","carrier","devicetype","deviceip","country","zipcode","geotype","campaignid","creativeid","Creativetype","creativecategory","outcome"]

allowed_cols_OW_traffictype = ["publisherid","appsiteid","appsitecategory","position","bidfloor","os","osvrsn","carrier","devicetype","deviceip","country","zipcode","campaignid","exchangebid","outcome"]#["publisherid","appsiteid","appsitecategory","position","timestamp","gender","os","osvrsn","model","manufacturer","carrier","devicetype","deviceip","country","zipcode","geotype","campaignid","creativeid","Creativetype","creativecategory","outcome"]
allowed_cols_OW_appsiteid = ["traffictype","publisherid","appsitecategory","position","bidfloor","os","osvrsn","carrier","devicetype","deviceip","country","zipcode","campaignid","exchangebid","outcome"] #["traffictype","publisherid","appsitecategory","position","timestamp","gender","os","osvrsn","model","manufacturer","carrier","devicetype","deviceip","country","zipcode","geotype","campaignid","creativeid","Creativetype","creativecategory","outcome"]
allowed_cols_OW_appsitecategory = ["traffictype","publisherid","appsiteid","position","bidfloor","os","osvrsn","carrier","devicetype","deviceip","country","zipcode","campaignid","exchangebid","outcome"] #["traffictype","publisherid","appsiteid","position","timestamp","gender","os","osvrsn","model","manufacturer","carrier","devicetype","deviceip","country","zipcode","geotype","campaignid","creativeid","Creativetype","creativecategory","exchangebid","outcome"]
allowed_cols_OW_campaignid = ["traffictype","publisherid","appsiteid","appsitecategory","position","bidfloor","os","osvrsn","carrier","devicetype","deviceip","country","zipcode","exchangebid","outcome"] #["traffictype","publisherid","appsiteid","appsitecategory","position","bidfloor","timestamp","age","gender","os","osvrsn","model","manufacturer","carrier","devicetype","deviceip","country","zipcode","geotype","creativeid","Creativetype","creativecategory","outcome"]
allowed_cols_OW_publisherid = ["traffictype","appsiteid","appsitecategory","position","bidfloor","os","osvrsn","carrier","devicetype","deviceip","country","zipcode","campaignid","exchangebid","outcome"] #["traffictype","appsiteid","appsitecategory","position","bidfloor","timestamp","age","gender","os","osvrsn","model","manufacturer","carrier","devicetype","deviceip","country","zipcode","geotype","campaignid","creativeid","Creativetype","creativecategory","outcome"]

if modeltype == "WC_traffictype":
    allowed_cols = allowed_cols_WC_traffictype
    country_pos = 13
    conjunction_arr = WC_Conjunctions
elif modeltype == "WC_appsiteid":
    allowed_cols = allowed_cols_WC_appsiteid
    country_pos = 13
    conjunction_arr = WC_Conjunctions
elif modeltype == "WC_appsitecategory":
    allowed_cols = allowed_cols_WC_appsitecategory
    country_pos = 13
    conjunction_arr = WC_Conjunctions
elif modeltype == "WC_campaignid":
    allowed_cols = allowed_cols_WC_campaignid
    country_pos = 14
    conjunction_arr = WC_Conjunctions
elif modeltype == "WC_publisherid":
    allowed_cols = allowed_cols_WC_publisherid
    country_pos = 13
    conjunction_arr = WC_Conjunctions
elif modeltype == "OW_appsiteid":
    country_pos = 10
    conjunction_arr = OW_Conjunctions
    allowed_cols = allowed_cols_OW_appsiteid
elif modeltype == "OW_appsitecategory":
    country_pos = 10
    conjunction_arr = OW_Conjunctions
    allowed_cols = allowed_cols_OW_appsitecategory
elif modeltype == "OW_campaignid":
    country_pos = 11
    conjunction_arr = OW_Conjunctions
    allowed_cols = allowed_cols_OW_campaignid
elif modeltype == "OW_publisherid":
    country_pos = 10
    conjunction_arr = OW_Conjunctions
    allowed_cols = allowed_cols_OW_publisherid
elif modeltype == "OW_traffictype":
    country_pos = 10
    conjunction_arr = OW_Conjunctions
    allowed_cols = allowed_cols_OW_traffictype

with open(trainfilename, "r") as data:
    for line in data:
        if header == False:
            header = True
            header_col = line.split(',')
        else:
            container = []
            cols = line.split(',')
            for c in range(0,len(cols)-1):
                col = cols[c]
                if header_col[c][1:-1] in allowed_cols:
                    try:
                        if header_col[c][1:-1] == "timestamp":
                            col = str(((int(col)/60)*60)/3600)+str(cols[country_pos])
                        hash_in = str(header_col[c][1:-1])+'|||'+str(col)
                        container.append(hash_in)
                    except:
                        print "[DEBUG]something went wrong with: "+str(c)+" value: "+str(col)
            for conj in conjunction_arr:
                conj1 = conj.split('###')[0]
                conj2 = conj.split('###')[1]
                conj1_val = cols[getpos(conj1,header_col)]
                conj2_val = cols[getpos(conj2,header_col)]
                hash_in = conj1+'|||'+str(conj1_val)+'###'+conj2+'|||'+str(conj2_val)
                container.append(hash_in)   
            x = get_x(container)
            p = get_p(x)
            #print "[INFO]train probability: "+str(p)
            target = str(cols[-1].strip()[1:-1])
            flag = 0
            if str(modeltype.split('_')[0]) == "WC":
                if "C" in target or "c" in target:
                    target = 1
                    flag = 1
                elif "W" in target or "w" in target:
                    target = 0
                    flag = 1
            elif str(modeltype.split('_')[0]) == "OW":
                if target == "W" or target == "w":
                    target = 1
                    flag = 1
                elif target == "0" or target == "O" or target == "o":
                    target = 0
                    flag = 1
            if flag == 1:
                #act.append((float(target),float(1-target)))
                #print "[INFO]target is: "+str(target)
                update_w(x,p,target)

header = False
header_col = []

f = open(submitfilename,'w')
print >> f, '"ID","target"'

with open(testfilename,"r") as testfile:
    for line in testfile:
        if header == False:
            header = True
            header_col = line.split(',')
        else:
            container = []
            cols = line.split(',')
            for c in range(0,len(cols)):
                col = cols[c]
                if header_col[c][1:-1] in allowed_cols:
                    try:
                        if header_col[c][1:-1] == "timestamp":
                            col = str(((int(col)/60)*60)/3600)+str(cols[country_pos])
                        hash_in = str(header_col[c][1:-1])+'|||'+str(col)
                        container.append(hash_in)
                    except:
                        print "[DEBUG]something went wrong with: "+str(c)+" value: "+str(col)
            for conj in conjunction_arr:
                conj1 = conj.split('###')[0]
                conj2 = conj.split('###')[1]
                try:
                    conj1_val = cols[getpos(conj1,header_col)]
                    conj2_val = cols[getpos(conj2,header_col)]
                    hash_in = conj1+'|||'+str(conj1_val)+'###'+conj2+'|||'+str(conj2_val)
                    container.append(hash_in)
                except:
                    None
            x = get_x(container)
            p = get_p(x)
            #print "[DEBUG]probability: "+str(p)
            #pred.append((float(p),float(1-p)))
            print >> f, str(cols[0])+','+str(p)

            target = str(cols[-1].strip()[1:-1])
            flag = 0
            if str(modeltype.split('_')[0]) == "WC":
                if "C" in target or "c" in target:
                    target = 1
                    flag = 1
                elif "W" in target or "w" in target:
                    target = 0
                    flag = 1
            elif str(modeltype.split('_')[0]) == "OW":
                if target == "W" or target == "w":
                    target = 1
                    flag = 1
                elif target == "0" or target == "O" or target == "o":
                    target = 0
                    flag = 1
            if flag == 1:
                act.append((float(target),float(1-target)))
                pred.append((float(p),float(1-p)))

print "[STATS]the logloss of the data: "
print "[STATS]"+str(llfun(act,pred))

print "[STATS]the 0/1 loss of the data: "
print "[STATS]" +str(O_ONE_LOSS(act,pred))




