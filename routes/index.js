module.exports = function(io, clothes) {	
	var express = require('express');
	var router = express.Router();

	router.get('/clothes/:id', function(req, res, next) {		
		if (Object.keys(clothes).indexOf(req.params.id) < 0) {
			clothes[req.params.id] = true;
		} else {
			clothes[req.params.id] = !clothes[req.params.id];
		}	
		console.log(clothes);
		process.emit('update-clothes', clothes);
		//socket.emit('clothes', clothes);
		res.end();	  		
	});	
  
	/* GET home page. */
	router.get('/', function(req, res, next) {
	  res.render('index', { title: 'Express' });
	});

	return router;
}
