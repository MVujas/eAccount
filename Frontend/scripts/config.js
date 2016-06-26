'use strict';

module.exports = [
  '$stateProvider',
  '$urlRouterProvider',
  function anaConfig($stateProvider, $urlRouterProvider){
    $urlRouterProvider.otherwise('/home/');
    $stateProvider
      .state('home', {
        url: '/home/',
        resolve: {
          config: ['anaService',
            function(anaService){
              return anaService.getConfig();
            }
          ]
        },
        controller: 'homeController',
        templateUrl: 'views/home.html',
        
      })
      .state('racun', {
        url: '/racun/',
        resolve: {
          prihodi: ['anaService',
            function(anaService){
              return anaService.getFunds();
            }
          ],
          troskovi: ['anaService',
            function(anaService){
              return anaService.getCosts();
            }
          ],
          radnici: ['anaService',
            function(anaService){
              return anaService.getWorkers();
            }
          ],
          config: ['anaService',
            function(anaService){
              return anaService.getConfig();
            }
          ]
        },
        controller: 'racunController',
        templateUrl: 'views/racun.html',
      })
      .state('radnici', {
        url: '/radnici/',
        resolve: {
          radnici: ['anaService',
            function(anaService){
              return anaService.getWorkers();
            }
          ],
          workerlists: ['anaService',
            function(anaService){
              return anaService.getWorkerLists();
            }
          ],
          config: ['anaService',
            function(anaService){
              return anaService.getConfig();
            }
          ]
        },
        controller: 'radniciController',
        templateUrl: 'views/radnici.html',
      })
      .state('troskovi', {
        url: '/troskovi/',
        resolve: {
          costs: ['anaService',
            function(anaService){
              return anaService.getCosts();
            }
          ],
          coststickets: ['anaService',
            function(anaService){
              return anaService.getCostsTicket();
            }
          ],
          config: ['anaService',
            function(anaService){
              return anaService.getConfig();
            }
          ]
        },
        controller: 'troskoviController',
        templateUrl: 'views/troskovi.html',
      })
      .state('prihodi', {
        url: '/prihodi/',
        resolve: {
          funds: ['anaService',
            function(anaService){
              return anaService.getFunds();
            }
          ],
          fundstickets: ['anaService',
            function(anaService){
              return anaService.getFundsTicket();
            }
          ],
          config: ['anaService',
            function(anaService){
              return anaService.getConfig();
            }
          ]
        },
        controller: 'prihodiController',
        templateUrl: 'views/prihodi.html',
      });
  }
]