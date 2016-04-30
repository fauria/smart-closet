var socket = io.connect('http://10.0.214.1:3000');
$(document).ready(function(){
	console.log('Document ready!');	
	socket.on('clothes', function (clothes) {
		console.log('Clothes received:');
		console.log(clothes);	
		Object.keys(clothes).forEach(function(uid){
			if(clothes[uid]) {
				$('#'+uid).fadeTo('slow', 0.2);
			}else{
				$('#'+uid).fadeTo('slow', 1);
			}
		});
	});	
});
	