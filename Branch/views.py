from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from Branch.forms import clusterForm
from Branch.models import Cluster
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="user:loginView")
def clusterView(request,clusterId,action):
  
    if clusterId != 0:   
        cluster_instance = Cluster.objects.get(id=clusterId)
    
    if request.method == "POST" and action == "add":
        form = clusterForm(data= request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cluster:clusterView',
            kwargs={"action":"view","clusterId":0}))
        else:
            return render(request,"cluster/cluster.html",
                  {"form":form,"clusterID":0})  
            
    if action == "edit":
        if request.method == "POST":
            form = clusterForm(data= request.POST,instance=cluster_instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('cluster:clusterView',
                        kwargs={"action":"view","clusterId":0}))
            else:
                return render(request,"cluster/cluster.html",
                  {"form":form,"clusterID":cluster_instance.id})
        else:
            return render(request,"cluster/cluster.html",
                  {"form":clusterForm(instance=cluster_instance),"clusterID":cluster_instance.id,"action":"edit"})
    
    if action == "delete":
        cluster_instance.delete()
        return HttpResponseRedirect(reverse('cluster:clusterView',
            kwargs={"action":"view","clusterId":0}))
                 
    return render(request,"cluster/cluster.html",
                  {"form":clusterForm(),"clusterID":0,"action":"add"})
