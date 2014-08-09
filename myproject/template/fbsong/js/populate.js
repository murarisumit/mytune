function populate(player)
{
	data=JSON.parse(document.getElementById("hdata").value);
	all_ids=data['all_ids']; //all the videos ID
	console.log(all_ids);
	playlist=data['feed_list'];
	for (var i=0; i<playlist.length; i++)
	{     
		var item=playlist[i];
		console.log(item['from']);
		console.log(item['name']);
		var html = '<li><a href="' +i+ '" class="videolink"> <i class="icon-play"></i> ' + item['name'] + '</a></li>';
		$('#videoslist').append(html);
	}
	player.loadPlaylist(all_ids);  
	
	$('.videolink').on('click', function(e) {
		e.preventDefault();
		var ind = parseInt($(this).attr('href'));
		console.log(ind);
		player.playVideoAt(ind);
	});
}
/*
 * 
* Working thing
alert("welcome populate.js");
alert(document.getElementById("hdata").value);
data=JSON.parse(document.getElementById("hdata").value);
alert(data);
all_ids=data['all_ids'];
alert(all_ids);
console.log(all_ids);
playlist=data['feed_list'];
for (var i=0; i<playlist.length; i++)
{     
	var item=playlist[i];
	console.log(item['from']);
	console.log(item['name']);
	var html = '<li><a href="' +i+ '" class="videolink"> <i class="icon-play"></i> ' + item['name'] + '</a></li>';
	$('#videoslist').append(html);
}
 //after all the work is done, add the songs to player.
player.loadPlaylist(all_ids);  
 
$('.videolink').on('click', function(e) {
e.preventDefault();
var ind = parseInt($(this).attr('href'));
console.log(ind);
player.playVideoAt(ind);
});
*/
