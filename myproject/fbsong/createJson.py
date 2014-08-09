import facebook
import json

def checkk():
	sumit="sumitmurari"
	return sumit


def get_feed_from_page2():
	"""This'll fetch the feeds from the pages"""
	graph=facebook.GraphAPI("CAACEdEose0cBAA1RZAKGdSZBiTxxUw4yBWvdqxko2Ag2VdYXS9FbOzCPZBSkMsYn5UKpJ84q1VcyKh9Wr2SZCgmapVzbzHe33V7Q1qT1SCQjVM0kvCcgDunOQlbXWHZAdh9sPoDSpfLkvFStLepIBptxQRjBv6IWZBt3cII9uBmVEmOqF1bzREGlC7veHGbXtqw3zQsQ1mDCelrrdoNMYaZArUdCkuYnfEZD")
	groupFeed = graph.get_connections('221723967989344','feed')  #(pageId,feed)
	feedData=groupFeed['data']
  
  #it'll save the feed list. It'll be list of hash's
	feed_list=[]
  
	#list to store all video's id:
	all_ids=[]
	for x in range(len(feedData)):
		#print "\nFor feed ",x
		#print feedData[x]
		feed_id=feedData[x]["id"]
		print "Feed id is: ",feed_id
		#we nneed source of the song ...  
		if feedData[x].has_key('source'):
			#print "Source is: "
			#print feedData[x]['source']
			d={}
			if feedData[x]['source'].find('http://www.youtube.com/v/') != -1:
				video_id=feedData[x]['source'].split('/v/')[1][:11]
				all_ids.append(video_id)
				
				if feedData[x]["name"]:
					escpdName=feedData[x]["name"].replace('\'','')
					d["name"]=escpdName
				d["from"]=video_id
				d["username"]=feedData[x]["from"]["name"]
				#d={ "from" : video_id,"username": feedData[x]["from"]["name"],"name" : feedData[x]["name"] }
				
				if feedData[x].has_key('description'):
					escpdDesc=feedData[x]["description"].replace('\'','')
					d["description"]=escpdDesc
				else:
					d["description"]=""
			
				if feedData[x].has_key('likes'):
					d["likes"]=len(feedData[x]['likes']['data'])
				else:
					#print "no like field found !"   # No like field found,hence 0 likes on the feed
					d["likes"]=0 
			feed_list.append(d)
	finalFeed={"feed_list":feed_list,"all_ids":all_ids }
	#Encode them in json_data
	json_string=json.dumps(finalFeed)
	print "Function work done...returning \n"
	return json_string
	

#json_data=get_feed_from_page2()
#print json_data


