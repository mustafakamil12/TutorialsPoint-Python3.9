/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/js/index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/js/index.js":
/*!*************************!*\
  !*** ./src/js/index.js ***!
  \*************************/
/*! no static exports found */
/***/ (function(module, exports) {

$ = jQuery;
$(document).ready(function () {
  // Tabs
  // Moved this in front of AOS because it was breaking the Product pages
  if ($(".sdk-tabs-container").length) {
    // console.log("TABS");
    $(".sdk-tabs-container").tabs();
  }

  if ($(".pricing-tabs").length) {
    // console.log("TABS");
    $("#pricing-tabs-container").tabs({
      event: "mouseover",
      active: 0
    });
  } // Accordions


  if ($("#pricing-tabs-container").length) {
    // console.log("accordions");
    $(".pricing-section__single button").click(function (e) {
      $(this).parent('.pricing-section__single').toggleClass('pricing-section__rows-active');
    });
  } // Initialize AOS


  if ($(".aos--flag").length) {
    // console.log("AOS");
    AOS.init({
      disable: 'mobile'
    });
  } // Dials 


  if ($(".roi-module").length) {
    // console.log("DIALS");
    function animateElements() {
      $('.progressbar').each(function () {
        var elementPos = $(this).offset().top;
        var topOfWindow = $(window).scrollTop();
        var percent = $(this).find('.circle').attr('data-percent');
        var hours = $(this).find('.circle').attr('data-hours');
        var percentage = parseInt(percent, 10) / parseInt(100, 10);
        var animate = $(this).data('animate');

        if (elementPos < topOfWindow + $(window).height() - 30 && !animate) {
          $(this).data('animate', true);
          $(this).find('.circle').circleProgress({
            startAngle: -Math.PI / 2,
            value: percent / 100,
            size: 120,
            thickness: 10,
            emptyFill: "#515151",
            fill: {
              color: '#00E5BF'
            }
          });
        }
      });
    } // Show animated elements


    animateElements();
    $(window).scroll(animateElements);
  } // Mega Menu


  $(window).scroll(function (event) {
    var scrollVal = $(window).scrollTop();

    if (scrollVal > 100) {
      if (!$("nav").hasClass('nav--light')) {
        // console.log('light menu');
        $("nav").addClass('nav--light');
        $(".nav-container").addClass('nav--light');
      }
    } else {
      if ($("nav").hasClass('nav--light')) {
        // console.log('reg menu');
        $("nav").removeClass('nav--light');
        $(".nav-container").removeClass('nav--light');
      }
    }
  }); // Desktop

  $('.nav__first-level__single__button').click(function (e) {
    var $this = $(this); // Check if nav backdrop is already open

    if ($(".nav__backdrop").hasClass('backdrop-active')) {
      // If the button's section is already open, close 
      if ($this.siblings('.nav__second-level').children(".second-level-abs").hasClass('secondary-menu-active')) {
        $(".nav__backdrop").removeClass('backdrop-active');
        $this.siblings('.nav__second-level').children(".second-level-abs").removeClass('secondary-menu-active');
        $this.siblings('.nav__second-level').children(".second-level-abs").addClass('secondary-menu-deactivate');
        $(".nav__backdrop__overlay").removeClass('overlay-active');
        $(".nav-item-arrow").removeClass('arrow-active');
      } else if (!$this.siblings('.nav__second-level').children(".second-level-abs").hasClass('secondary-menu-active')) {
        // If the button's section is not open, but the backdrop is open, it must be another item that wants to open so, just fade in the new section
        $(".second-level-abs").removeClass('secondary-menu-active');
        $(".nav-item-arrow").removeClass('arrow-active');
        $(".second-level-abs").removeClass('secondary-menu-deactivate');
        $this.siblings('.nav__second-level').children(".second-level-abs").addClass('secondary-menu-active');
        $this.children('.nav-item-arrow').addClass('arrow-active');
      } else {
        return;
      }
    } else {
      // If not open, open and activate section 
      $(".nav__backdrop__overlay").addClass('overlay-active');
      $(".nav__backdrop").addClass('backdrop-active');
      $this.siblings('.nav__second-level').children(".second-level-abs").addClass('secondary-menu-active');
      $this.siblings('.nav__second-level').children(".second-level-abs").removeClass('secondary-menu-deactivate');
      $this.children('.nav-item-arrow').addClass('arrow-active');
    }
  }); // Click overlay to exit

  $(".nav__backdrop__overlay").click(function (e) {
    $(this).removeClass('overlay-active');
    $(".nav__backdrop").removeClass('backdrop-active');
    $(".second-level-abs").removeClass('secondary-menu-active');
    $(".second-level-abs").addClass('secondary-menu-deactivate');
    $(".nav-item-arrow").removeClass('arrow-active');
  }); // Mobile

  $('.mobile-trigger').click(function (e) {
    $('.mobile-dropdown').toggleClass('active-mobile-dropdown');
    $('body').toggleClass('no-scroll-body');
    $('#mobile-menu-icon').toggleClass('open');
  });
  $('.dropdown__single__button').click(function (e) {
    var $this = $(this);
    $(".nav-item-arrow").removeClass('arrow-active');

    if ($this.siblings(".dropdown__single__list").hasClass('active-mobile-list')) {
      $this.siblings(".dropdown__single__list").removeClass('active-mobile-list');
    } else {
      $(".dropdown__single__list").removeClass('active-mobile-list');
      $this.siblings(".dropdown__single__list").addClass('active-mobile-list');
      $this.children('.nav-item-arrow').addClass('arrow-active');
    }
  }); // Count

  if ($("#counter").length && !$(".stats--custom").length) {
    // console.log("COUNTER 1");
    var a = 0;
    $(window).scroll(function () {
      var oTop = $('#counter').offset().top - window.innerHeight;

      if (a == 0 && $(window).scrollTop() > oTop) {
        $('.counter-value').each(function () {
          var $this = $(this),
              countTo = $this.attr('data-count');
          $({
            countNum: $this.text()
          }).animate({
            countNum: countTo
          }, {
            duration: 1500,
            easing: 'swing',
            step: function step() {
              if ($this.attr('data-type') == 'thousand') {
                $this.text(Math.ceil(this.countNum).toLocaleString('en'));
              } else {
                $this.text(Math.floor(this.countNum));
              }
            },
            complete: function complete() {
              if ($this.attr('data-type') == 'thousand') {
                $this.text(Math.ceil(this.countNum).toLocaleString('en'));
              } else {
                $this.text(this.countNum);
              } //alert('finished');

            }
          });
        });
        a = 1;
      }
    });
  } // Count - Specific Case (1.2B)


  if ($(".stats--custom").length) {
    // console.log("COUNTER 2");
    var a = 0;
    $(window).scroll(function () {
      var oTop = $('#counter').offset().top - window.innerHeight;

      if (a == 0 && $(window).scrollTop() > oTop) {
        $('.stats__single:not(#stats__single--2) .counter-value').each(function () {
          var $this = $(this),
              countTo = $this.attr('data-count');
          $({
            countNum: $this.text()
          }).animate({
            countNum: countTo
          }, {
            duration: 1500,
            easing: 'swing',
            step: function step() {
              if ($this.attr('data-type') == 'thousand') {
                $this.text(Math.ceil(this.countNum).toLocaleString('en'));
              } else {
                $this.text(Math.floor(this.countNum));
              }
            },
            complete: function complete() {
              if ($this.attr('data-type') == 'thousand') {
                $this.text(Math.ceil(this.countNum).toLocaleString('en'));
              } else {
                $this.text(this.countNum);
              } //alert('finished');

            }
          });
        });

        if ($("#stats__single--2").length) {
          $('#stats__single--2 .counter-value').each(function () {
            var $this = $(this),
                countTo = $this.attr('data-count');
            $({
              countNum: 400
            }).animate({
              countNum: 1000
            }, {
              duration: 1500,
              easing: 'swing',
              step: function step() {
                $this.text(Math.floor(this.countNum));
                $this.siblings('.stats__single__suffix').text('M');
              },
              complete: function complete() {
                $this.text(countTo);
                $this.siblings('.stats__single__suffix').text('B');
              }
            });
          });
        }

        a = 1;
      }
    });
  } // Count - Hero


  if ($(".stats--hero").length && !$(".stats--custom-hero").length) {
    console.log("COUNTER HERO 1");
    $('.counter-value').each(function () {
      var $this = $(this),
          countTo = $this.attr('data-count');
      $({
        countNum: $this.text()
      }).animate({
        countNum: countTo
      }, {
        duration: 1500,
        easing: 'swing',
        step: function step() {
          if ($this.attr('data-type') == 'thousand') {
            $this.text(Math.ceil(this.countNum).toLocaleString('en'));
          } else {
            $this.text(Math.floor(this.countNum));
          }
        },
        complete: function complete() {
          if ($this.attr('data-type') == 'thousand') {
            $this.text(Math.ceil(this.countNum).toLocaleString('en'));
          } else {
            $this.text(this.countNum);
          } //alert('finished');

        }
      });
    });
  } // Count - Specific Case (1.2B) - HERO


  if ($(".stats--custom-hero").length) {
    console.log("COUNTER HERO 2");
    $('.stats__single:not(#stats__single--2) .counter-value').each(function () {
      var $this = $(this),
          countTo = $this.attr('data-count');
      $({
        countNum: $this.text()
      }).animate({
        countNum: countTo
      }, {
        duration: 1500,
        easing: 'swing',
        step: function step() {
          if ($this.attr('data-type') == 'thousand') {
            $this.text(Math.ceil(this.countNum).toLocaleString('en'));
          } else {
            $this.text(Math.floor(this.countNum));
          }
        },
        complete: function complete() {
          if ($this.attr('data-type') == 'thousand') {
            $this.text(Math.ceil(this.countNum).toLocaleString('en'));
          } else {
            $this.text(this.countNum);
          } //alert('finished');

        }
      });
    });

    if ($("#stats__single--2").length) {
      $('#stats__single--2 .counter-value').each(function () {
        var $this = $(this),
            countTo = $this.attr('data-count');
        $({
          countNum: 400
        }).animate({
          countNum: 1000
        }, {
          duration: 1500,
          easing: 'swing',
          step: function step() {
            $this.text(Math.floor(this.countNum));
            $this.siblings('.stats__single__suffix').text('M');
          },
          complete: function complete() {
            $this.text(countTo);
            $this.siblings('.stats__single__suffix').text('B');
          }
        });
      });
    }
  } // Mega Tabs


  if ($(".mega-tabs-module").length) {
    // console.log('MEGA TABS');
    var mainContainer = document.getElementById('mega-tabs__content-container');
    var contentContainerInitial = document.getElementById('mega-tabs-content--hidden-1');
    var megaTabsActive = 1;
    mainContainer.innerHTML = contentContainerInitial.innerHTML;
    $('#mega-tabs__btn-1').hover(function (e) {
      // console.log('hover1');
      var contentContainer = document.getElementById('mega-tabs-content--hidden-1');

      if (megaTabsActive != 1) {
        megaTabsActive = 1;
        $('#mega-tabs__content-container').fadeOut("fast", function () {
          mainContainer.innerHTML = contentContainer.innerHTML;
          $('#mega-tabs__content-container').fadeIn("fast");
        });
      }

      $('.mega-tabs-button').removeClass("mega-tabs-button--active");
      $(this).addClass("mega-tabs-button--active");
    });
    $('#mega-tabs__btn-2').hover(function (e) {
      // console.log('hover2');
      var contentContainer = document.getElementById('mega-tabs-content--hidden-2');

      if (megaTabsActive != 2) {
        megaTabsActive = 2;
        $('#mega-tabs__content-container').fadeOut("fast", function () {
          mainContainer.innerHTML = contentContainer.innerHTML;
          $('#mega-tabs__content-container').fadeIn("fast");
        });
      }

      $('.mega-tabs-button').removeClass("mega-tabs-button--active");
      $(this).addClass("mega-tabs-button--active");
    });
    $('#mega-tabs__btn-3').hover(function (e) {
      // console.log('hover3');
      var contentContainer = document.getElementById('mega-tabs-content--hidden-3');

      if (megaTabsActive != 3) {
        megaTabsActive = 3;
        $('#mega-tabs__content-container').fadeOut("fast", function () {
          mainContainer.innerHTML = contentContainer.innerHTML;
          $('#mega-tabs__content-container').fadeIn("fast");
        });
      }

      $('.mega-tabs-button').removeClass("mega-tabs-button--active");
      $(this).addClass("mega-tabs-button--active");
    });
    $('#mega-tabs__btn-1').click(function (e) {
      var contentContainer = document.getElementById('mega-tabs-content--hidden-1');

      if (megaTabsActive != 1) {
        megaTabsActive = 1;
        $('#mega-tabs__content-container').fadeOut("fast", function () {
          mainContainer.innerHTML = contentContainer.innerHTML;
          $('#mega-tabs__content-container').fadeIn("fast");
        });
      }

      $('.mega-tabs-button').removeClass("mega-tabs-button--active");
      $(this).addClass("mega-tabs-button--active");
    });
    $('#mega-tabs__btn-2').click(function (e) {
      var contentContainer = document.getElementById('mega-tabs-content--hidden-2');

      if (megaTabsActive != 2) {
        megaTabsActive = 2;
        $('#mega-tabs__content-container').fadeOut("fast", function () {
          mainContainer.innerHTML = contentContainer.innerHTML;
          $('#mega-tabs__content-container').fadeIn("fast");
        });
      }

      $('.mega-tabs-button').removeClass("mega-tabs-button--active");
      $(this).addClass("mega-tabs-button--active");
    });
    $('#mega-tabs__btn-3').click(function (e) {
      var contentContainer = document.getElementById('mega-tabs-content--hidden-3');

      if (megaTabsActive != 3) {
        megaTabsActive = 3;
        $('#mega-tabs__content-container').fadeOut("fast", function () {
          mainContainer.innerHTML = contentContainer.innerHTML;
          $('#mega-tabs__content-container').fadeIn("fast");
        });
      }

      $('.mega-tabs-button').removeClass("mega-tabs-button--active");
      $(this).addClass("mega-tabs-button--active");
    });
  } // PDF


  if ($(".pdf-cta").length) {
    $('.pdf-cta').click(function (e) {
      // console.log('pdf form');
      e.preventDefault();
      var email_popup = $('.email-popup');
      var body = $('body');
      email_popup.remove();
      body.prepend("<div class='popup-background active'></div>");
      body.prepend(email_popup);
      email_popup.addClass('active');
      $('.close-popup').click(function () {
        $('.popup-background').remove();
        email_popup.removeClass('active');
      });
      $('.popup-background').click(function () {
        $(this).remove();
        email_popup.removeClass('active');
      });
    });
    MktoForms2.loadForm("//app-sj28.marketo.com", "857-LSW-455", 1215, function (form) {
      form.onSuccess(function (values, followUpUrl) {
        var vals = form.vals();
      });
    });
  } // ROI Calc


  if ($(".service-providers").length) {
    // console.log('ROI CALC PAGE');
    jQuery(".service-providers input[type='checkbox']").attr("checked", true);
    jQuery(".submit-providers").click(function () {
      jQuery("#calculator-form").submit();
    });
    jQuery(".service-providers input[type='checkbox']").change(function () {
      if (jQuery(".service-providers input[type='checkbox']").is(":checked")) {
        jQuery(".submit-providers").removeClass("secondary_button_white");
        jQuery(".submit-providers").addClass("primary_button_green");
      } else {
        jQuery(".submit-providers").addClass("secondary_button_white");
        jQuery(".submit-providers").removeClass("primary_button_green");
      }
    });
    /*jQuery(".select-providers").click(function() {
        jQuery(".service-providers input[type='checkbox']").attr("checked", true); 
        jQuery(".submit-providers").removeClass("secondary_button_white");
        jQuery(".submit-providers").addClass("primary_button_green");
        jQuery(".ex-email-tracking-lb").removeClass("blocked");
        jQuery(".g-email-tracking-lb").removeClass("blocked");
        jQuery(".oo-email-tracking-lb").removeClass("blocked");
     });*/

    jQuery("#g-email-sync").change(function () {
      if (jQuery("#g-email-sync").is(":checked")) {
        jQuery(".g-email-tracking-lb").removeClass("blocked");
      } else {
        jQuery("#g-email-tracking").attr("checked", false);
        jQuery(".g-email-tracking-lb").addClass("blocked");
      }
    });
    jQuery("#ex-email-sync").change(function () {
      if (jQuery("#ex-email-sync").is(":checked")) {
        jQuery(".ex-email-tracking-lb").removeClass("blocked");
      } else {
        jQuery("#ex-email-tracking").attr("checked", false);
        jQuery(".ex-email-tracking-lb").addClass("blocked");
      }
    });
    jQuery("#oo-email-sync").change(function () {
      if (jQuery("#oo-email-sync").is(":checked")) {
        jQuery(".oo-email-tracking-lb").removeClass("blocked");
      } else {
        jQuery("#oo-email-tracking").attr("checked", false);
        jQuery(".oo-email-tracking-lb").addClass("blocked");
      }
    });
  } // ROI Modals


  if ($(".title-task").length) {
    $(".content-task .title-task").click(function () {
      modal = $(this).data("name");
      $("#myModal-" + modal).css("display", "flex");
    });
    $(".modal-task .close-modal").click(function () {
      $(this).parent().parent().css("display", "none");
    });
  } // Swiper


  if ($(".swiper-container").length) {
    var swiper = new Swiper('.swiper-container', {
      effect: 'coverflow',
      grabCursor: true,
      centeredSlides: true,
      spaceBetween: -10,
      slidesPerView: 1.25,
      loop: true,
      initialSlide: 1,
      coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 1000,
        modifier: 1,
        slideShadows: true
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
      }
    });
  } // Blog search


  if ($("#blog-search-form").length) {
    // console.log("search");
    $(".blog-search-trigger").click(function (e) {
      // console.log('click trigger')
      $('#blog-search-form').toggleClass('search-form-hidden');
    });
  } // GDPR


  if ($("#gdpr-container").length) {
    // console.log("GDPR");
    var message = getCookie();

    if (message != 'ok') {
      $('#gdpr-container').slideDown(1000);
    } else {
      $('#gdpr-container').slideUp(1000);
    }
    /* GDPR SCRIPT METHODS */
    // $("#close-cookies").click(() => {
    //     console.log('GDPR notice');
    //     setCookie('ok');
    //     $('#gdpr-container').slideDown(1000);
    // });


    $("#close-cookies").click(function (e) {
      console.log('GDPR notice');
      setCookie('ok');
      $('#gdpr-container').addClass('hide-gdpr');
    });

    function setCookie(cvalue) {
      var now = new Date();
      var time = now.getTime();
      var expireTime = time + 90 * 86400000;
      now.setTime(expireTime);
      document.cookie = "cookiegdpr=" + cvalue + ";expires=" + now.toGMTString() + ";path=/";
    }

    function getCookie() {
      var name = "cookiegdpr=";
      var decodedCookie = decodeURIComponent(document.cookie);
      var ca = decodedCookie.split(';');

      for (var i = 0; i < ca.length; i++) {
        var c = ca[i];

        while (c.charAt(0) == ' ') {
          c = c.substring(1);
        }

        if (c.indexOf(name) == 0) {
          return c.substring(name.length, c.length);
        }
      }

      return "";
    }
    /* END GDPR SCRIPT */

  } // Social Share


  if ($(".nylas-social-share").length) {
    // console.log('sharing');
    function ss_click(width, height) {
      var leftPosition, topPosition; //Allow for borders.

      leftPosition = window.screen.width / 2 - (width / 2 + 10); //Allow for title and status bars.

      topPosition = window.screen.height / 2 - (height / 2 + 50);
      var windowFeatures = "status=no,height=" + height + ",width=" + width + ",resizable=yes,left=" + leftPosition + ",top=" + topPosition + ",screenX=" + leftPosition + ",screenY=" + topPosition + ",toolbar=no,menubar=no,scrollbars=no,location=no,directories=no";
      u = location.href;
      t = document.title;
      window.open('http://www.facebook.com/sharer.php?u=' + encodeURIComponent(u) + '&t=' + encodeURIComponent(t), 'sharer', windowFeatures);
      return false;
    }
  } // Platform Overview Scroll Module


  if ($(".platform-triangle__single").length) {
    // Smooth Scroll
    var speed = 500;
    $('a[href*="#"]').filter(function (i, a) {
      return a.getAttribute('href').startsWith('#') || a.href.startsWith("".concat(location.href, "#"));
    }).unbind('click.smoothScroll').bind('click.smoothScroll', function (event) {
      var targetId = event.currentTarget.getAttribute('href').split('#')[1];
      var targetElement = document.getElementById(targetId);

      if (targetElement) {
        event.preventDefault();
        $('html, body').animate({
          scrollTop: $(targetElement).offset().top
        }, speed);
      }
    });
    $(window).scroll(function () {
      var windowBottom = $(this).scrollTop() + $(this).height();
      var elementTop = $("#platform-cards-desktop").offset().top;
      var percentage = (windowBottom - elementTop) / $("#platform-cards-desktop").height() * 100;

      if (percentage > 90) {
        // console.log(percentage, '5 end - UX');
        $('.platform-triangle__single').removeClass('platform-triangle__single--active');
        $('.platform-overview__content__single').removeClass('platform-overview__content__single--active');
        $('.platform-triangle__single:nth-child(1)').addClass('platform-triangle__single--active');
        $('#user-experience').next().addClass('platform-overview__content__single--active');
      } else if (percentage < 90 && percentage > 70) {
        // console.log(percentage, '4 - auto');
        $('.platform-triangle__single').removeClass('platform-triangle__single--active');
        $('.platform-overview__content__single').removeClass('platform-overview__content__single--active');
        $('.platform-triangle__single:nth-child(2)').addClass('platform-triangle__single--active');
        $('#automation').next().addClass('platform-overview__content__single--active');
      } else if (percentage < 70 && percentage > 50) {
        // console.log(percentage, '3 - intel');
        $('.platform-triangle__single').removeClass('platform-triangle__single--active');
        $('.platform-overview__content__single').removeClass('platform-overview__content__single--active');
        $('.platform-triangle__single:nth-child(3)').addClass('platform-triangle__single--active');
        $('#intelligence').next().addClass('platform-overview__content__single--active');
      } else if (percentage < 50 && percentage > 30) {
        // console.log(percentage, '2 - security');
        $('.platform-triangle__single').removeClass('platform-triangle__single--active');
        $('.platform-overview__content__single').removeClass('platform-overview__content__single--active');
        $('.platform-triangle__single:nth-child(4)').addClass('platform-triangle__single--active');
        $('#security').next().addClass('platform-overview__content__single--active');
      } else {
        // console.log(percentage, '1 start - connectivity');
        $('.platform-triangle__single').removeClass('platform-triangle__single--active');
        $('.platform-overview__content__single').removeClass('platform-overview__content__single--active');
        $('.platform-triangle__single:nth-child(5)').addClass('platform-triangle__single--active');
        $('#connectivity').next().addClass('platform-overview__content__single--active');
      }
    });
  } // Google Web Vitals


  function sendToGTM(_ref) {
    var name = _ref.name,
        delta = _ref.delta,
        id = _ref.id;
    // console.log(name, delta, id);
    // Assumes the global `dataLayer` array exists, see:
    // https://developers.google.com/tag-manager/devguide
    dataLayer.push({
      event: 'web-vitals',
      event_category: 'Web Vitals',
      event_action: name,
      // Google Analytics metrics must be integers, so the value is rounded.
      // For CLS the value is first multiplied by 1000 for greater precision
      // (note: increase the multiplier for greater precision if needed).
      event_value: Math.round(name === 'CLS' ? delta * 1000 : delta),
      // The `id` value will be unique to the current page load. When sending
      // multiple values from the same page (e.g. for CLS), Google Analytics can
      // compute a total by grouping on this ID (note: requires `eventLabel` to
      // be a dimension in your report).
      event_label: id // eventCallback: function() {
      //     console.log("GWV");
      // }

    });
  }

  webVitals.getCLS(sendToGTM);
  webVitals.getFID(sendToGTM);
  webVitals.getLCP(sendToGTM);
  webVitals.getTTFB(sendToGTM);
  webVitals.getFCP(sendToGTM); // Local Storage

  if ($(".local-storage-check").length) {
    localStorage.setItem('dashboardCheck', 'true');
  }
});

/***/ })

/******/ });
//# sourceMappingURL=build.js.map