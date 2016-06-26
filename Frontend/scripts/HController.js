'use strict'

module.exports = [
  '$scope',
  'config',
  'anaService',
  '$window',
  function($scope, config, anaService, $window){
    $scope.config = config.data[0];
    $scope.lang = ($scope.config.lang == "rs") ? "rs" : "en";
    $scope.text = ($scope.config.lang == "rs") ? require('../lang/rs.js') : require('../lang/en.js');
  
      
  }
];