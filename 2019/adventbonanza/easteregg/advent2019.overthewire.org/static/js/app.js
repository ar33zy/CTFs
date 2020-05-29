var ChallengeUpdateInterval = 60; // seconds
var app = angular.module('advent', ['ui.bootstrap']);

app.controller('ModalCtrl', function($scope, $uibModal, $http, $timeout) {
  $scope.expectedChallengeCount = 24;
  $scope.challenges = [];
  var oldChallengesStr = JSON.stringify($scope.challenges);
  $scope.lockedCount = -1;
  $scope.showsanta = false;

  var processInputData = function(data) {
	for (var i = 0; i < data.length; i++) {
		if(window.localStorage["opened-" + i] && data[i]["state"] == "unopened") {
			data[i]["state"] = "opened";
		}
		if(data[i].state == "completed") {
			data[i]["class"] = "opened completed";
		} else {
			data[i]["class"] = data[i]["state"];
		}
	}
        var currlength = data.length;
        var daycount = 25;
	for (var i = currlength; i < daycount; i++) {
	    var datestr = "2018-12-";
	    if((i+1) < 10) datestr += "0";
	    datestr += ""+(i+1);
	    data[i] = {
		"name": "",
		"date": datestr,
		"state": "locked",
		"category": "",
		"points": 0,
		"info": "",
		"author": "",
		"play_url": "",
		"download_url": ""
	    }
	}
	return data;
  };

  var rememberOpened = function(idx) {
	var chal = $scope.challenges[idx];
	window.localStorage["opened-" + idx] = true;
  };

  var rerenderDoors = function() {
      $timeout(function() {
		  $scope.challenges = processInputData($scope.challenges);
	  }, 100);
  };

  var updateChallenges = function() {
	$http({
		 method: 'GET',
		   url: '/challenges.json'
	  }).then(function successCallback(response) {
		var tmpChallenges = processInputData(response.data);
		var newChallengesStr = JSON.stringify(tmpChallenges);
		if(oldChallengesStr != newChallengesStr) {
		  $scope.challenges = tmpChallenges;
		  oldChallengesStr = newChallengesStr;
		  $timeout(function() {
			  updateCSSPositions();
		  }, 0);
		  checkNewChallenges();
		}
		$timeout(updateChallenges, 1000 * ChallengeUpdateInterval);
	  }, function errorCallback(response) {
		console.log("Error retrieving challenges.json");
	});
  };

  window.updateChallenges = updateChallenges;

  var checkNewChallenges = function() {
	var lockedcount = 0;
	for (var i = 0; i < $scope.challenges.length; i++) {
	  if($scope.challenges[i]["state"] == "locked") {
		lockedcount += 1;
	  }
	}

	console.log("scope lockedcount = "+$scope.lockedCount+" and lockedcount = "+lockedcount);

	if(lockedcount != $scope.lockedCount) {
	  if($scope.lockedCount != -1) {
	        if(localStorage.getItem("gfx") != 2) {
		    var audio = new Audio('/static/audio/santabells.mp3');
		    audio.play();
		    $scope.showsanta = true;
		    console.log("GFX enabled");
		} else {
		    console.log("GFX disabled");
		}
		console.log("Detected new unlocked challenges");
	  }
	  $scope.lockedCount = lockedcount;
    }
  }

  $scope.open = function(idx) {
	var chal = $scope.challenges[idx];

	// if it's locked, don't open it
	if(chal && chal.state == "locked"){
		toast('Hold your horses cowboy, that is still locked.');
		return;
	}
	
	// remember that we opened it...
	rememberOpened(idx);
	rerenderDoors();

/*    var modalInstance =  $uibModal.open({
      templateUrl: "/static/popup.html",
      controller: "ModalContentCtrl",
      size: '',
      resolve: {
		  data: function() {
			  return $scope.challenges[idx];
		  }
	  }
    });

	modalInstance.result.then(function(response){
		if(response == "solved") {
			chal.state = "completed";
			rerenderDoors();
		}
	});*/
  }


  // after the animation, hide santa
  document.getElementById("santa").addEventListener("animationend", function() {
      $timeout(function() {
		  $scope.showsanta = false;
		  location.reload(); 
	  }, 100);
  });


  updateChallenges();
})

app.controller('ModalContentCtrl', function($scope, $uibModalInstance, data) {
  $scope.data = data;

  $scope.submitflag = function(){
	  alert("submitting flag...");
      $uibModalInstance.close("solved");
  }
  
});
