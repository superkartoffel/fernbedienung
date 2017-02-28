var http = require('http');
var exec = require('child_process').exec, child;
var execSync = require('sync-exec');
var fs = require('fs')

function readFile(file) {
    if ((file=='') || (file=='/')) {
        file = "index.html";
    }
    var content = '';
    try {
        content = fs.readFileSync('/home/pi/webserver/html/'+file);
    } catch (err) {
        return "404 - not found";
    }
    return content;
    
}

function getContentType(file) {
    var def = 'text/html';
    var ext = file.match(/.*\.(\w+)$/);
    if (!ext) 
        return def;
    
    switch (ext[1]) {
        case 'ico':
            return 'image/x-icon';
        default:
            return def;
    }
}

http.createServer(function (req, res) {
    console.log('Request: '+req.url);
    
    var file = req.url.match(/^\/([^\/^?^&]*)$/);
    
    if (file) {        
        console.log('File: '+file[1]);
        res.writeHead(200, {'Content-Type': getContentType(file[1]) });
        res.end(readFile(file[1]));
        return;
    }
	var cmd = req.url.match(/cmd=(\w*)&/);
	if (!cmd) {
	    res.writeHead(200, {'Content-Type': 'text/html'});
	    res.end(readFile());
		return;
    }
	console.log('Processing: cmd='+cmd[1]);
	switch (cmd[1]) {
		/*case 'light':
			var light = req.url.match(/light=(\d)/);
			var state = req.url.match(/state=(1|0)/);
			if (state) {
				console.log('Light: '+light[1] + ', State: ' + state[1]); 
				child = exec('sudo /home/pi/raspberry-remote/send 11010 '+light[1]+' '+state[1], logIO);
        	}
			break;*/
			
		case 'youtube':
			var url = req.url.match(/url=(.*)/);
			if (url) {
				var decoded = decodeURIComponent(url[1]);
				console.log('Youtube: '+decoded); 
				child = exec('pkill omxplayer; youtube-dl -g "'+decoded+ '" | xargs omxplayer ', logIO);
        	}
			break;
			
		case 'run':
			var line = req.url.match(/line=(.*)/);
			if (line) {
				var decoded = decodeURIComponent(line[1]);
				console.log('Run: '+decoded); 
				child = exec(decoded, logIO);
        	}
			break;
			
			
		case 'call':
			var line = req.url.match(/line=(.*)/);
			if (line) {
				var decoded = decodeURIComponent(line[1]);
				console.log('Run: '+decoded); 
				try {
				    var logs = execSync(decoded, 30000);
				    console.log(logs);
	                res.writeHead(200, {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}); //'text/html'});//
	                res.end(logs.stdout);
	            } catch (err) {
	                console.log(err);
	                res.writeHead(504);
	                res.end();
	            }
        	}
			break;
			
		default:
	}
	res.writeHead(302, {
     'Location': '/'
    });
    res.end();
}).listen(80);

function logIO(error, stdout, stderr) {
	console.log('stdout: ' + stdout);
	console.log('stderr: ' + stderr);
	if (error !== null) {
		console.log('exec error: ' + error);
	}
}
