var Utility = {
  getPosition : function(el){
    var oL = el.offsetLeft, oT = el.offsetTop;
    var oE = el;
    while(oE = oE.offsetParent){
      oL = oL + oE.offsetLeft;
      oT = oT + oE.offsetTop;
    }        
    return [oL, oT];
  },

  getDocSize : function() {
    var D = document;
    var H = Math.max(
      Math.max(D.body.scrollHeight, D.documentElement.scrollHeight),
      Math.max(D.body.offsetHeight, D.documentElement.offsetHeight),
      Math.max(D.body.clientHeight, D.documentElement.clientHeight)
    );
    var W = Math.max(
      Math.max(D.body.scrollWidth, D.documentElement.scrollWidth),
      Math.max(D.body.offsetWidth, D.documentElement.offsetWidth),
      Math.max(D.body.clientWidth, D.documentElement.clientWidth)
    );
    return [W,H];
  },
  // Detect what gradient syntax is supported and return an
  // array with [GRADIENT_STYLE, PREFIX] or an empty array if
  // gradients are not supported.
  // GRADIENT_STYLE is either "webkit" or "w3c"
  detectGradientSyntax : function(){
    var syntaxCheck = document.createElement('syntax');

    var prefixes = ["", "-webkit-", "-moz-", "-ms-", "-o-"];                            
    while((checkPrefix = prefixes.shift()) != undefined) {   
      syntaxCheck.style.backgroundImage = checkPrefix + 'linear-gradient(left top,#9f9, white)';
      if(syntaxCheck.style.backgroundImage.indexOf( 'linear' ) !== -1) {
        break
      }
    }

    if(checkPrefix == undefined){
      // Check for old-style webkit syntax
      syntaxCheck.style.backgroundImage = '-webkit-gradient(linear,left top,right bottom,from(#9f9),to(white))';
      if(syntaxCheck.style.backgroundImage.indexOf( 'webkit' ) !== -1) {
        return ["webkit", null]
      } else {
       return []; 
      }
    } else {
      return ["w3c", checkPrefix];                
    }

  },
  // Detect css prefix to use for a certain feature
  detectCssPrefix : function(feature){    
    var syntaxCheck = document.createElement('syntax');    
    if(syntaxCheck.style[feature] != undefined){
      return feature;
    }
    
    var fName = feature[0].toUpperCase() + feature.substr(1)
    var prefixes = ["Webkit", "Moz", "ms", "O"];                            
    while((checkPrefix = prefixes.shift()) != undefined) { 
      if(syntaxCheck.style[checkPrefix + fName] != undefined) {
        break
      }
    }
    
    if(checkPrefix == undefined){
      // No cigar...
      return ""
    } else {
      return checkPrefix + fName;
    }   
  }
};
   

var updateCSSPositions = (function(){
  
  var calcCSSPositions = function(){
    var els = document.querySelectorAll(".doors li .door");

    var bgOff = getBgOffsets();
    
    str = [];
    for(var i=0; i < els.length; i++){
      var el = els[i];
      // Get position from top-left
      var elPos = Utility.getPosition(el);
      str.push(".doors li:nth-child("+(i+1)+") .door { background-position: 0 0, " + -1* (elPos[0] + -1*bgOff[0]) + "px " + -1 * (elPos[1] + -1*bgOff[1]) + "px}");    
    }

    return str;
  }
  
  var getBgOffsets = function(){
    // Get background position
    var bgW = 1698, bgH = 1131;

    var docS = Utility.getDocSize();
    var leftO = 0; //docS[0]/2 - bgW/2;
    var topO = 0; // FIXME
    return [leftO, topO];
  }
  
  var setPositions = function(){
    var els = document.querySelectorAll(".doors li .door");

    var bgOff = getBgOffsets();
    
    for(var i=0; i < els.length; i++){
      var el = els[i];
      var elPos = Utility.getPosition(el);
      el.style.backgroundPosition = "0 0, " + -1* (elPos[0] + -1*bgOff[0]) + "px " + -1 * (elPos[1] + -1*bgOff[1]) + "px";        
      
    }          
    
  }
  
  window.onresize = setPositions;
  return setPositions;
  //document.addEventListener("DOMContentLoaded", setPositions, false);
          
})();
