from bs4 import BeautifulSoup  

html_data = """ 
<!DOCTYPE html>

<html lang="en" dir="ltr"

>



<head>

  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="https://www.mosdac.gov.in/favicon.ico" type="image/vnd.microsoft.icon" />
<link rel="search" type="application/opensearchdescription+xml" title="MOSDAC" href="/apios/osdd.xml" />
<meta name="title" content="Meteorological and Oceanographic Satellite Data Archival Centre (MOSDAC)" />
<meta name="description" content="Megha- Tropiques (MT) is a joint Indo-French collaborative satellite mission, which is launched on 12 October 2011." />
<meta name="abstract" content="Meteorological and Oceanographic Satellite Data Archival Centre (MOSDAC) is a Data Centre of Space Applications Centre (SAC) and has facility for satellite data reception, processing, analysis and dissemination. MOSDAC is operationally supplying earth observation data from Indian meteorology and oceanography satellites." />
<meta name="keywords" content="Meteorological, Oceanographic, Satellite, Data, Archival, Data Centre" />
<meta name="generator" content="MOSDAC" />
<link rel="canonical" href="https://www.mosdac.gov.in/bayesian-based-mt-saphir-rainfall?language=en" />
<link rel="shortlink" href="https://www.mosdac.gov.in/node/1225?language=en" />
    <!--<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">-->

    <meta name="MobileOptimized" content="width" />

    <meta name="HandheldFriendly" content="true" />

    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <meta name="lang" content="en" />

<!--<meta http-equiv="cleartype" content="on" />-->

  <title>Bayesian based MT-SAPHIR rainfall | Meteorological & Oceanographic Satellite Data Archival Centre</title>

  <link type="text/css" rel="stylesheet" href="https://www.mosdac.gov.in/sites/default/files/css/css_xE-rWrJf-fncB6ztZfd2huxqgxu4WO-qwma6Xer30m4.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://www.mosdac.gov.in/sites/default/files/css/css_vvSDwk3p1t-3F5SmIcvQLDZ3qfg7ElFEStQfHSnQc1Y.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://www.mosdac.gov.in/sites/default/files/css/css_aT6E7gfTnF0UQzS_3tbtH4DdzyMXdWUcYzjsKqfmCA8.css" media="all" />
<style type="text/css" media="all">
<!--/*--><![CDATA[/*><!--*/
#back-top{right:40px;}#back-top span#button{background-color:#CCCCCC;}#back-top span#button:hover{opacity:1;background-color:#777777;}

/*]]>*/-->
</style>
<link type="text/css" rel="stylesheet" href="https://www.mosdac.gov.in/sites/default/files/css/css_vTQ0ibuAz81WT3Y2frKQ26Ht5Wzg6khM2J8T3QxSAoQ.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://www.mosdac.gov.in/sites/default/files/css/css_Pwl7HgjSRlYXkkBCMM47QG1eRVAPexaRiW9aM4Ec2c4.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://www.mosdac.gov.in/sites/default/files/css/css_2THG1eGiBIizsWFeexsNe1iDifJ00QRS9uSd03rY9co.css" media="print" />
  <script type="text/javascript">
<!--//--><![CDATA[//><!--
var highContrast = {"link":"<a href=\"\/?language=en\" class=\"element-invisible element-focusable\" rel=\"nofollow\">Toggle high contrast<\/a>","cssFilePath":"https:\/\/www.mosdac.gov.in\/sites\/default\/files\/high_contrast_current.css"};var drupalHighContrast={};!function(){document.write("<script type='text/javascript' id='high-contrast-css-placeholder'>\x3C/script>");var e=document.getElementById("high-contrast-css-placeholder");!function(e){if("function"==typeof define&&define.amd)define(e);else if("object"==typeof exports)module.exports=e();else{var t=window.Cookies,n=window.Cookies=e();n.noConflict=function(){return window.Cookies=t,n}}}(function(){function e(){for(var e=0,t={};e<arguments.length;e++){var n=arguments[e];for(var o in n)t[o]=n[o]}return t}function t(n){function o(t,r,i){var a;if(arguments.length>1){if(i=e({path:"/"},o.defaults,i),"number"==typeof i.expires){var d=new Date;d.setMilliseconds(d.getMilliseconds()+864e5*i.expires),i.expires=d}try{a=JSON.stringify(r),/^[\{\[]/.test(a)&&(r=a)}catch(c){}return r=encodeURIComponent(String(r)),r=r.replace(/%(23|24|26|2B|3A|3C|3E|3D|2F|3F|40|5B|5D|5E|60|7B|7D|7C)/g,decodeURIComponent),t=encodeURIComponent(String(t)),t=t.replace(/%(23|24|26|2B|5E|60|7C)/g,decodeURIComponent),t=t.replace(/[\(\)]/g,escape),document.cookie=[t,"=",r,i.expires&&"; expires="+i.expires.toUTCString(),i.path&&"; path="+i.path,i.domain&&"; domain="+i.domain,i.secure?"; secure":""].join("")}t||(a={});for(var l=document.cookie?document.cookie.split("; "):[],s=/(%[0-9A-Z]{2})+/g,u=0;u<l.length;u++){var f=l[u].split("="),h=f[0].replace(s,decodeURIComponent),g=f.slice(1).join("=");'"'===g.charAt(0)&&(g=g.slice(1,-1));try{if(g=n&&n(g,h)||g.replace(s,decodeURIComponent),this.json)try{g=JSON.parse(g)}catch(c){}if(t===h){a=g;break}t||(a[h]=g)}catch(c){}}return a}return o.get=o.set=o,o.getJSON=function(){return o.apply({json:!0},[].slice.call(arguments))},o.defaults={},o.remove=function(t,n){o(t,"",e(n,{expires:-1}))},o.withConverter=t,o}return t()});var t=function(e){var t={option:[1,"<select multiple='multiple'>","</select>"],legend:[1,"<fieldset>","</fieldset>"],area:[1,"<map>","</map>"],param:[1,"<object>","</object>"],thead:[1,"<table>","</table>"],tr:[2,"<table><tbody>","</tbody></table>"],col:[2,"<table><tbody></tbody><colgroup>","</colgroup></table>"],td:[3,"<table><tbody><tr>","</tr></tbody></table>"],_default:[1,"<div>","</div>"]};t.optgroup=t.option,t.tbody=t.tfoot=t.colgroup=t.caption=t.thead,t.th=t.td;var n=document.createElement("div"),o=/<\s*\w.*?>/g.exec(e);if(null!=o){var n,r=o[0].replace(/</g,"").replace(/>/g,""),i=t[r]||t._default;e=i[1]+e+i[2],n.innerHTML=e;for(var a=i[0]+1;a--;)n=n.lastChild}else n.innerHTML=e,n=n.lastChild;return n};!function(){function e(){if(!o.isReady){try{document.documentElement.doScroll("left")}catch(t){return void setTimeout(e,1)}o.ready()}}var t,n,o=function(e,t){},r=(window.jQuery,window.$,!1),i=[];o.fn={ready:function(e){return o.bindReady(),o.isReady?e.call(document,o):i&&i.push(e),this}},o.isReady=!1,o.ready=function(){if(!o.isReady){if(!document.body)return setTimeout(o.ready,13);if(o.isReady=!0,i){for(var e,t=0;e=i[t++];)e.call(document,o);i=null}o.fn.triggerHandler&&o(document).triggerHandler("ready")}},o.bindReady=function(){if(!r){if(r=!0,"complete"===document.readyState)return o.ready();if(document.addEventListener)document.addEventListener("DOMContentLoaded",n,!1),window.addEventListener("load",o.ready,!1);else if(document.attachEvent){document.attachEvent("onreadystatechange",n),window.attachEvent("onload",o.ready);var t=!1;try{t=null==window.frameElement}catch(i){}document.documentElement.doScroll&&t&&e()}}},t=o(document),document.addEventListener?n=function(){document.removeEventListener("DOMContentLoaded",n,!1),o.ready()}:document.attachEvent&&(n=function(){"complete"===document.readyState&&(document.detachEvent("onreadystatechange",n),o.ready())}),window.jQuery=window.$=o}();var n=function(){var e=document.getElementById("block-delta-blocks-logo"),t=highContrast.logoPath;if(document.querySelectorAll&&"undefined"!=typeof t&&null!==e){var n=e.querySelectorAll("img");"undefined"==typeof n[0].logoPathOriginal&&(n[0].logoPathOriginal=n[0].src),n[0].src=t}},o=function(){var e=document.getElementById("block-delta-blocks-logo"),t=highContrast.logoPath;if(document.querySelectorAll&&"undefined"!=typeof t&&null!==e){var n=e.querySelectorAll("img");"undefined"!=typeof n[0].logoPathOriginal&&(n[0].src=n[0].logoPathOriginal)}},r=function(){var o=highContrast.cssFilePath;if("undefined"!=typeof o){var r=document.getElementById("high-contrast-css");null===r&&(r=t('<link type="text/css" id="high-contrast-css" rel="stylesheet" href="'+o+'" media="screen" />')),e.parentNode.insertBefore(r,e.nextSibling)}n(),Cookies.set("highContrastActivated","true","/")},i=function(){var e=document.getElementById("high-contrast-css");null!==e&&e.parentNode.removeChild(e),o(),Cookies.set("highContrastActivated","false","/")},a=function(){var e=Cookies.get("highContrastActivated");return"undefined"==typeof e?!1:"false"===e?!1:!0},d=function(){a()?(i(),Cookies.set("highContrastActivated","false","/")):(r(),Cookies.set("highContrastActivated","true","/"))},c=function(){var e=highContrast.link;e=t(e),e.onclick=function(){return d(),this.blur(),!1},document.getElementById("skip-link").appendChild(e)};drupalHighContrast.enableStyles=r,drupalHighContrast.disableStyles=i,drupalHighContrast.toggleHighContrast=d,a()&&r(),$.fn.ready(function(){a()&&n(),c()})}();

//--><!]]>
</script>
<script type="text/javascript" src="https://www.mosdac.gov.in/sites/default/files/js/js_HdPbt6gVMRWegeXlF6t6-licjnoFrOBSDkur0NWOI48.js"></script>
<script type="text/javascript" src="https://www.mosdac.gov.in/sites/default/files/js/js_WwwX68M9x5gJGdauMeCoSQxOzb1Ebju-30k5FFWQeH0.js"></script>
<script type="text/javascript" src="https://www.mosdac.gov.in/sites/default/files/js/js_D6I6wkKerbOLVJccDLVgJTQxezQzv_kXBd9CgjY1BcE.js"></script>
<script type="text/javascript" src="https://www.mosdac.gov.in/sites/default/files/js/js_efKhfF-_xr6KiPJbxUL_CQ2QiIwScZ5dyjiWbEijFvU.js"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
var text_resize_scope = "header, a, p, footer-line, footer-wrapper, span";
          var text_resize_minimum = "10";
          var text_resize_maximum = "20";
          var text_resize_line_height_allow = 0;
          var text_resize_line_height_min = "16";
          var text_resize_line_height_max = "36";
//--><!]]>
</script>
<script type="text/javascript" src="https://www.mosdac.gov.in/sites/default/files/js/js_lRERpfq1LKFWK6ORKnY-VfIk5EYeqTcLdzW6dZRcjNg.js"></script>
<script type="text/javascript" src="https://www.mosdac.gov.in/sites/default/files/js/js_nfn0IaR4ywK9HErZfH51r1l81weRTh6JsEhqA-O3LjU.js"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
jQuery.extend(Drupal.settings, {"basePath":"\/","pathPrefix":"","setHasJsCookie":0,"ajaxPageState":{"theme":"my_theme","theme_token":"4WgQ91Wn4O7KrFtRD6sHFPztsyAneLFwlPp2EC5sMJE","js":{"0":1,"sites\/all\/modules\/jquery_update\/replace\/jquery\/3.5\/jquery.min.js":1,"misc\/jquery-extend-3.4.0.js":1,"misc\/jquery-html-prefilter-3.5.0-backport.js":1,"misc\/jquery.once.js":1,"misc\/drupal.js":1,"sites\/all\/modules\/jquery_update\/replace\/ui\/external\/jquery.cookie.js":1,"misc\/form-single-submit.js":1,"sites\/all\/modules\/views_slideshow_xtra\/views_slideshow_xtra_overlay\/js\/views_slideshow_xtra_overlay.js":1,"sites\/all\/modules\/iframe\/iframe.js":1,"sites\/all\/modules\/lightbox2\/js\/lightbox.js":1,"sites\/all\/modules\/scroll_to_top\/scroll_to_top.js":1,"1":1,"sites\/all\/modules\/text_resize\/text_resize.js":1,"sites\/all\/modules\/lang_dropdown\/lang_dropdown.js":1,"sites\/all\/modules\/extlink\/js\/extlink.js":1,"sites\/all\/modules\/intlink\/js\/intlink.js":1,"sites\/all\/libraries\/superfish\/jquery.hoverIntent.minified.js":1,"sites\/all\/libraries\/superfish\/sfsmallscreen.js":1,"sites\/all\/libraries\/superfish\/supposition.js":1,"sites\/all\/libraries\/superfish\/superfish.js":1,"sites\/all\/libraries\/easing\/jquery.easing.js":1,"sites\/all\/libraries\/superfish\/supersubs.js":1,"sites\/all\/modules\/superfish\/superfish.js":1,"sites\/all\/themes\/responsive_bartik\/js\/collapsible-menu.js":1},"css":{"modules\/system\/system.base.css":1,"modules\/system\/system.menus.css":1,"modules\/system\/system.messages.css":1,"modules\/system\/system.theme.css":1,"sites\/all\/modules\/scroll_to_top\/scroll_to_top.css":1,"modules\/aggregator\/aggregator.css":1,"modules\/comment\/comment.css":1,"modules\/field\/theme\/field.css":1,"sites\/all\/modules\/filebrowser\/css\/filebrowser_style.css":1,"modules\/node\/node.css":1,"modules\/search\/search.css":1,"modules\/user\/user.css":1,"sites\/all\/modules\/views_slideshow_xtra\/views_slideshow_xtra_overlay\/css\/views_slideshow_xtra_overlay.css":1,"sites\/all\/modules\/extlink\/css\/extlink.css":1,"modules\/forum\/forum.css":1,"sites\/all\/modules\/views\/css\/views.css":1,"sites\/all\/modules\/intlink\/css\/intlink.css":1,"sites\/all\/modules\/ctools\/css\/ctools.css":1,"sites\/all\/modules\/high_contrast\/high_contrast.css":1,"sites\/all\/modules\/lightbox2\/css\/lightbox.css":1,"0":1,"sites\/all\/modules\/text_resize\/text_resize.css":1,"modules\/locale\/locale.css":1,"sites\/all\/modules\/views_fluid_grid\/css\/views_fluid_grid.base.css":1,"sites\/all\/modules\/views_fluid_grid\/css\/views_fluid_grid.size.css":1,"sites\/all\/modules\/lang_dropdown\/lang_dropdown.css":1,"sites\/all\/modules\/social_media_links\/social_media_links.css":1,"sites\/all\/libraries\/superfish\/css\/superfish.css":1,"sites\/all\/libraries\/superfish\/css\/superfish-smallscreen.css":1,"sites\/all\/libraries\/superfish\/style\/blue.css":1,"sites\/all\/themes\/responsive_bartik\/css\/layout.css":1,"sites\/all\/themes\/responsive_bartik\/css\/style.css":1,"sites\/all\/themes\/my_theme\/css\/colors.css":1,"sites\/all\/themes\/my_theme\/css\/custom.css":1,"sites\/all\/themes\/my_theme\/css\/hover.css":1,"sites\/all\/themes\/responsive_bartik\/css\/print.css":1}},"lightbox2":{"rtl":"0","file_path":"\/(\\w\\w\/)public:\/","default_image":"\/sites\/all\/modules\/lightbox2\/images\/brokenimage.jpg","border_size":10,"font_color":"000","box_color":"fff","top_position":"","overlay_opacity":"0.8","overlay_color":"000","disable_close_click":true,"resize_sequence":0,"resize_speed":400,"fade_in_speed":400,"slide_down_speed":600,"use_alt_layout":false,"disable_resize":false,"disable_zoom":false,"force_show_nav":false,"show_caption":true,"loop_items":false,"node_link_text":"View Image Details","node_link_target":false,"image_count":"Image !current of !total","video_count":"Video !current of !total","page_count":"Page !current of !total","lite_press_x_close":"press \u003Ca href=\u0022#\u0022 onclick=\u0022hideLightbox(); return FALSE;\u0022\u003E\u003Ckbd\u003Ex\u003C\/kbd\u003E\u003C\/a\u003E to close","download_link_text":"","enable_login":false,"enable_contact":false,"keys_close":"c x 27","keys_previous":"p 37","keys_next":"n 39","keys_zoom":"z","keys_play_pause":"32","display_image_size":"original","image_node_sizes":"()","trigger_lightbox_classes":"","trigger_lightbox_group_classes":"","trigger_slideshow_classes":"","trigger_lightframe_classes":"","trigger_lightframe_group_classes":"","custom_class_handler":0,"custom_trigger_classes":"","disable_for_gallery_lists":true,"disable_for_acidfree_gallery_lists":true,"enable_acidfree_videos":true,"slideshow_interval":5000,"slideshow_automatic_start":true,"slideshow_automatic_exit":true,"show_play_pause":true,"pause_on_next_click":false,"pause_on_previous_click":true,"loop_slides":false,"iframe_width":600,"iframe_height":400,"iframe_border":1,"enable_video":false,"useragent":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/91.0.4472.124 Safari\/537.36"},"scroll_to_top":{"label":"Back to top"},"urlIsAjaxTrusted":{"\/bayesian-based-mt-saphir-rainfall?language=en":true},"superfish":{"1":{"id":"1","sf":{"animation":{"opacity":"show","height":["show","easeInOutBounce"]},"speed":"fast"},"plugins":{"smallscreen":{"mode":"window_width","breakpointUnit":"px","accordionButton":"0","title":"\u0026#9776; Menu"},"supposition":true,"supersubs":true}}},"extlink":{"extTarget":"_blank","extClass":"ext","extLabel":"(link is external)","extImgClass":0,"extIconPlacement":"append","extSubdomains":1,"extExclude":"","extInclude":".external.|.ftp\\:. |.filebrowser.|.tar.|.zip.|.jar.","extCssExclude":"","extCssExplicit":"","extAlert":"_blank","extAlertText":"REDIRECTION: This link will take you to an external website. Users caution is advised.","mailtoClass":0,"mailtoLabel":"(link sends e-mail)","extUseFontAwesome":false},"intlink":{"extTarget":"_blank","extClass":0,"extLabel":"(link is external)","extImgClass":0,"extIconPlacement":0,"extSubdomains":1,"extExclude":"","extInclude":".internal.|.pdf|.flip-book.|.xml|.tar.|.*jar.|.zip.|Software.","extCssExclude":"","extCssExplicit":"","extAlert":0,"extAlertText":"This link will take you to an external web site.","mailtoClass":0,"mailtoLabel":"(link sends e-mail)","extUseFontAwesome":0}});
//--><!]]>
</script>
  <!--[if (gte IE 6)&(lte IE 8)]>

    <script src="/sites/all/themes/responsive_bartik/js/selectivizr-min.js"></script>

  <![endif]-->

  <!--[if lt IE 9]>

    <script src="/sites/all/themes/responsive_bartik/js/html5-respond.js"></script>

  <![endif]-->

</head>

<body class="html not-front not-logged-in no-sidebars page-node page-node- page-node-1225 node-type-article i18n-en featured footer-columns" >

  <!--<div id="skip-link">

    <a href="#main-content" class="element-invisible element-focusable">Skip to main content</a>

  </div>-->

    <div id="page-wrapper"><div id="page">

       <div id="sticky"><div class="section clearfix">

        <div class="region region-sticky">
    <div id="block-block-12" class="block block-block">

    
  <div class="content">
    <p><a style="color: #095cb1;" title="Skip to main Content" href="#main-content">Skip to main Content</a></p>
  </div>
</div>
<div id="block-text-resize-0" class="block block-text-resize">

    
  <div class="content">
    <a href="javascript:;" class="changer" id="text_resize_decrease"><sup>-</sup>A</a> <a href="javascript:;" class="changer" id="text_resize_reset">A</a> <a href="javascript:;" class="changer" id="text_resize_increase"><sup>+</sup>A</a><div id="text_resize_clear"></div>  </div>
</div>
<div id="block-high-contrast-high-contrast-switcher" class="block block-high-contrast">

    
  <div class="content">
    
    <div class="high_contrast_switcher high_contrast_switcher_links">
        <span class="high_contrast_switcher_high"><a href="javascript:drupalHighContrast.enableStyles()" class="contrast_high">A</a></span><span class="high_contrast_switcher_normal"><a href="javascript:drupalHighContrast.disableStyles()" class="contrast_low">A</a></span>
    </div>
      </div>
</div>
<div id="block-lang-dropdown-language-content" class="block block-lang-dropdown">

    
  <div class="content">
    <form class="lang_dropdown_form language_content" id="lang_dropdown_form_language_content" action="/bayesian-based-mt-saphir-rainfall?language=en" method="post" accept-charset="UTF-8"><div><div class="form-item form-type-select form-item-lang-dropdown-select">
 <select class="lang-dropdown-select-element form-select" id="lang-dropdown-select-language_content" style="width:148px" name="lang_dropdown_select"><option value="hi">हिन्दी</option><option value="en" selected="selected">English</option></select>
</div>
<input type="hidden" name="hi" value="/?language=hi" />
<input type="hidden" name="en" value="/?language=en" />
<noscript><div>
<input type="submit" id="edit-submit" name="op" value="Go" class="form-submit" />
</div></noscript><input type="hidden" name="form_build_id" value="form-qKZY5yTW3Acb3H45tJlbCKdp1sLz_jsq8AgC_pnv_HM" />
<input type="hidden" name="form_id" value="lang_dropdown_form" />
</div></form>  </div>
</div>
  </div>
    </div></div> <!-- /.section, /#featured -->

  

  <header id="header" role="banner" class="with-secondary-menu"><div class="section clearfix">

          <nav id="secondary-menu" role="navigation" class="navigation">

        <h2 class="element-invisible">Secondary menu</h2><ul id="secondary-menu-links" class="links inline clearfix"><li class="menu-1926 first"><a href="/internal/registration?language=en" title="">SignUp</a></li>
<li class="menu-1925"><a href="/internal/uops?language=en" title="">Login</a></li>
<li class="menu-2914 last"><a href="/internal/logout?language=en" title="">Logout</a></li>
</ul>      </nav> <!-- /#secondary-menu -->

        

    

          <a href="/?language=en" title="Home" rel="home" id="logo">

        <img src="https://www.mosdac.gov.in/sites/default/files/mosdac_small.png" alt="Home" />

      </a>

    

          <div id="name-and-slogan">



                              <div id="site-name">

              <strong>

                <a href="/?language=en" title="Home" rel="home"><span>Meteorological &amp; Oceanographic Satellite Data Archival Centre</span></a>

              </strong>

            </div>

                  

                  <div id="site-slogan">

            Space Applications Centre, ISRO          </div>

        

      </div> <!-- /#name-and-slogan -->

    

    

          <nav id="main-menu" role="navigation" class="navigation">

              </nav> <!-- /#main-menu -->

      </div></header> <!-- /.section, /#header -->



      <div id="featured"><div class="section clearfix">

        <div class="region region-featured">
    <div id="block-superfish-1" class="block block-superfish">

    
  <div class="content">
    <ul  id="superfish-1" class="menu sf-menu sf-main-menu sf-horizontal sf-style-blue sf-total-items-10 sf-parent-items-5 sf-single-items-5"><li id="menu-219-1" class="first odd sf-item-1 sf-depth-1 sf-no-children"><a href="/?language=en" title="" class="sf-depth-1">Home</a></li><li id="menu-1427-1" class="middle even sf-item-2 sf-depth-1 sf-total-children-9 sf-parent-children-0 sf-single-children-9 menuparent"><a href="#" onclick="return false;" title="" class="sf-depth-1 menuparent nolink" tabindex="0">Missions</a><ul><li id="menu-1938-1" class="first odd sf-item-1 sf-depth-2 sf-no-children"><a href="/insat-3dr?language=en" class="sf-depth-2">INSAT-3DR</a></li><li id="menu-1697-1" class="middle even sf-item-2 sf-depth-2 sf-no-children"><a href="/insat-3d?language=en" class="sf-depth-2">INSAT-3D</a></li><li id="menu-1692-1" class="middle odd sf-item-3 sf-depth-2 sf-no-children"><a href="/kalpana-1?language=en" title="" class="sf-depth-2">KALPANA-1</a></li><li id="menu-1693-1" class="middle even sf-item-4 sf-depth-2 sf-no-children"><a href="/insat-3a?language=en" title="" class="sf-depth-2">INSAT-3A</a></li><li id="menu-1695-1" class="middle odd sf-item-5 sf-depth-2 sf-no-children"><a href="/megha-tropiques?language=en" title="" class="sf-depth-2">MeghaTropiques</a></li><li id="menu-1694-1" class="middle even sf-item-6 sf-depth-2 sf-no-children"><a href="/saral-altika?language=en" title="" class="sf-depth-2">SARAL-AltiKa</a></li><li id="menu-1696-1" class="middle odd sf-item-7 sf-depth-2 sf-no-children"><a href="/oceansat-2?language=en" title="" class="sf-depth-2">OCEANSAT-2</a></li><li id="menu-2976-1" class="middle even sf-item-8 sf-depth-2 sf-no-children"><a href="/oceansat-3?language=en" title="" class="sf-depth-2">OCEANSAT-3</a></li><li id="menu-2997-1" class="last odd sf-item-9 sf-depth-2 sf-no-children"><a href="/scatsat-1?language=en" title="" class="sf-depth-2">SCATSAT-1</a></li></ul></li><li id="menu-1674-1" class="middle odd sf-item-3 sf-depth-1 sf-total-children-3 sf-parent-children-0 sf-single-children-3 menuparent"><a href="#" onclick="return false;" title="" class="sf-depth-1 menuparent nolink" tabindex="0">Catalog</a><ul><li id="menu-2574-1" class="first odd sf-item-1 sf-depth-2 sf-no-children"><a href="/internal/catalog-satellite?language=en" title="" class="sf-depth-2">Satellite</a></li><li id="menu-2866-1" class="middle even sf-item-2 sf-depth-2 sf-no-children"><a href="/internal/catalog-insitu?language=en" title="" class="sf-depth-2">Insitu (AWS)</a></li><li id="menu-2867-1" class="last odd sf-item-3 sf-depth-2 sf-no-children"><a href="/internal/catalog-radar?language=en" title="" class="sf-depth-2">RADAR</a></li></ul></li><li id="menu-1501-1" class="middle even sf-item-4 sf-depth-1 sf-total-children-5 sf-parent-children-0 sf-single-children-5 menuparent"><a href="#" onclick="return false;" title="" class="sf-depth-1 menuparent nolink" tabindex="0">Galleries</a><ul><li id="menu-2568-1" class="first odd sf-item-1 sf-depth-2 sf-no-children"><a href="/internal/gallery?language=en" title="" class="sf-depth-2">Satellite Products</a></li><li id="menu-1875-1" class="middle even sf-item-2 sf-depth-2 sf-no-children"><a href="/internal/gallery/weather?language=en" title="" class="sf-depth-2">Weather Forecast</a></li><li id="menu-1699-1" class="middle odd sf-item-3 sf-depth-2 sf-no-children"><a href="/internal/gallery/ocean?language=en" title="" class="sf-depth-2">Ocean Forecast</a></li><li id="menu-2573-1" class="middle even sf-item-4 sf-depth-2 sf-no-children"><a href="/internal/gallery/dwr?language=en" title="" class="sf-depth-2">RADAR (DWR)</a></li><li id="menu-1874-1" class="last odd sf-item-5 sf-depth-2 sf-no-children"><a href="/internal/gallery/current?language=en" title="" class="sf-depth-2">Global Ocean Current</a></li></ul></li><li id="menu-1426-1" class="active-trail middle odd sf-item-5 sf-depth-1 sf-total-children-5 sf-parent-children-1 sf-single-children-4 menuparent"><a href="#" onclick="return false;" title="" class="sf-depth-1 menuparent nolink" tabindex="0">Data Access</a><ul><li id="menu-2862-1" class="first odd sf-item-1 sf-depth-2 sf-no-children"><a href="/internal/uops?language=en" title="" class="sf-depth-2">Order Data</a></li><li id="menu-1474-1" class="active-trail middle even sf-item-2 sf-depth-2 sf-total-children-3 sf-parent-children-3 sf-single-children-0 menuparent"><a href="#" onclick="return false;" title="" class="sf-depth-2 menuparent nolink" tabindex="0">Open Data</a><ul><li id="menu-2980-1" class="active-trail first odd sf-item-1 sf-depth-3 sf-total-children-4 sf-parent-children-0 sf-single-children-4 menuparent"><a href="#" onclick="return false;" title="" class="sf-depth-3 menuparent nolink" tabindex="0">Atmosphere</a><ul><li id="menu-2983-1" class="active-trail first odd sf-item-1 sf-depth-4 sf-no-children"><a href="/bayesian-based-mt-saphir-rainfall?language=en" title="" class="sf-depth-4 active">Bayesian based MT-SAPHIR rainfall</a></li><li id="menu-2981-1" class="middle even sf-item-2 sf-depth-4 sf-no-children"><a href="/gps-derived-integrated-water-vapour?language=en" title="" class="sf-depth-4">GPS derived Integrated water vapour</a></li><li id="menu-2982-1" class="middle odd sf-item-3 sf-depth-4 sf-no-children"><a href="/gsmap-isro-rain?language=en" title="" class="sf-depth-4">GSMap ISRO Rain</a></li><li id="menu-2984-1" class="last even sf-item-4 sf-depth-4 sf-no-children"><a href="/meteosat8-cloud-properties?language=en" title="" class="sf-depth-4">METEOSAT8 Cloud Properties</a></li></ul></li><li id="menu-2985-1" class="middle even sf-item-2 sf-depth-3 sf-total-children-4 sf-parent-children-0 sf-single-children-4 menuparent"><a href="#" onclick="return false;" title="" class="sf-depth-3 menuparent nolink" tabindex="0">Land</a><ul><li id="menu-2986-1" class="first odd sf-item-1 sf-depth-4 sf-no-children"><a href="/3d-volumetric-terls-dwrproduct?language=en" title="" class="sf-depth-4">3D Volumetric TERLS DWRproduct</a></li><li id="menu-2989-1" class="middle even sf-item-2 sf-depth-4 sf-no-children"><a href="/inland-water-height?language=en" title="" class="sf-depth-4">Inland Water Height</a></li><li id="menu-2988-1" class="middle odd sf-item-3 sf-depth-4 sf-no-children"><a href="/river-discharge?language=en" title="" class="sf-depth-4">River Discharge</a></li><li id="menu-2987-1" class="last even sf-item-4 sf-depth-4 sf-no-children"><a href="/soil-moisture-0?language=en" title="" class="sf-depth-4">Soil Moisture</a></li></ul></li><li id="menu-2990-1" class="last odd sf-item-3 sf-depth-3 sf-total-children-6 sf-parent-children-0 sf-single-children-6 menuparent"><a href="#" onclick="return false;" title="" class="sf-depth-3 menuparent nolink" tabindex="0">Ocean</a><ul><li id="menu-2995-1" class="first odd sf-item-1 sf-depth-4 sf-no-children"><a href="/global-ocean-surface-current?language=en" title="" class="sf-depth-4">Global Ocean Surface Current</a></li><li id="menu-2993-1" class="middle even sf-item-2 sf-depth-4 sf-no-children"><a href="/indian-mainland-coastal-product?language=en" title="" class="sf-depth-4">Indian Mainland Coastal Product</a></li><li id="menu-2991-1" class="middle odd sf-item-3 sf-depth-4 sf-no-children"><a href="/ocean-subsurface?language=en" title="" class="sf-depth-4">Ocean Subsurface</a></li><li id="menu-2992-1" class="middle even sf-item-4 sf-depth-4 sf-no-children"><a href="/oceanic-eddies-detection?language=en" title="" class="sf-depth-4">Oceanic Eddies Detection</a></li><li id="menu-2994-1" class="middle odd sf-item-5 sf-depth-4 sf-no-children"><a href="/sea-ice-occurrence-probability?language=en" title="" class="sf-depth-4">Sea Ice Occurrence Probability</a></li><li id="menu-2996-1" class="last even sf-item-6 sf-depth-4 sf-no-children"><a href="/wave-based-renewable-energy?language=en" title="" class="sf-depth-4">Wave based Renewable Energy</a></li></ul></li></ul></li><li id="menu-2844-1" class="middle odd sf-item-3 sf-depth-2 sf-no-children"><a href="/internal/calval-data?language=en" title="" class="sf-depth-2">Cal-Val</a></li><li id="menu-2845-1" class="middle even sf-item-4 sf-depth-2 sf-no-children"><a href="/internal/forecast-menu?language=en" title="" class="sf-depth-2">Forecast</a></li><li id="menu-1983-1" class="last odd sf-item-5 sf-depth-2 sf-no-children"><a href="/rss-feed?language=en" title="ISROCast" class="sf-depth-2">RSS Feeds</a></li></ul></li><li id="menu-2949-1" class="middle even sf-item-6 sf-depth-1 sf-total-children-4 sf-parent-children-1 sf-single-children-3 menuparent"><a href="#" onclick="return false;" title="" class="sf-depth-1 menuparent nolink" tabindex="0">Reports</a><ul><li id="menu-2863-1" class="first odd sf-item-1 sf-depth-2 sf-total-children-2 sf-parent-children-0 sf-single-children-2 menuparent"><a href="#" onclick="return false;" title="" class="sf-depth-2 menuparent nolink" tabindex="0">Calibration</a><ul><li id="menu-2343-1" class="first odd sf-item-1 sf-depth-3 sf-no-children"><a href="/insitu?language=en" class="sf-depth-3">Insitu</a></li><li id="menu-2136-1" class="last even sf-item-2 sf-depth-3 sf-no-children"><a href="/calibration-reports?language=en" title="" class="sf-depth-3">Relative</a></li></ul></li><li id="menu-1879-1" class="middle even sf-item-2 sf-depth-2 sf-no-children"><a href="/validation-reports?language=en" title="" class="sf-depth-2">Validation</a></li><li id="menu-2135-1" class="middle odd sf-item-3 sf-depth-2 sf-no-children"><a href="/data-quality?language=en" title="" class="sf-depth-2">Data Quality</a></li><li id="menu-2865-1" class="last even sf-item-4 sf-depth-2 sf-no-children"><a href="/weather-reports?language=en" class="sf-depth-2">Weather</a></li></ul></li><li id="menu-2570-1" class="middle odd sf-item-7 sf-depth-1 sf-no-children"><a href="/atlases?language=en" class="sf-depth-1">Atlases</a></li><li id="menu-1814-1" class="middle even sf-item-8 sf-depth-1 sf-no-children"><a href="/tools?language=en" title="" class="sf-depth-1">Tools</a></li><li id="menu-1978-1" class="middle odd sf-item-9 sf-depth-1 sf-no-children"><a href="/sitemap?language=en" title="" class="sf-depth-1">Sitemap</a></li><li id="menu-2979-1" class="last even sf-item-10 sf-depth-1 sf-no-children"><a href="/help?language=en" title="" class="sf-depth-1">Help</a></li></ul>  </div>
</div>
  </div>
    </div></div> <!-- /.section, /#featured -->

    

    

  <div id="main-wrapper" class="clearfix"><div id="main" role="main" class="clearfix">



    <h2 class="element-invisible">You are here</h2><div class="breadcrumb"><a href="/?language=en">Home</a> » <a href="#" onclick="return false;" title="" class="nolink" tabindex="0">Data Access</a> » <a href="#" onclick="return false;" title="" class="nolink" tabindex="0">Open Data</a> » <a href="#" onclick="return false;" title="" class="nolink" tabindex="0">Atmosphere</a> » Bayesian based MT-SAPHIR rainfall</div>

<div id="smart">



  

</div>



    <div id="content" class="column">

	<div class="section">

            <a id="main-content"></a>

            <h1 class="title" id="page-title">Bayesian based MT-SAPHIR rainfall</h1>            <div class="tabs"><h2 class="element-invisible">Primary tabs</h2><ul class="tabs primary"><li class="active"><a href="/bayesian-based-mt-saphir-rainfall?language=en" class="active">View<span class="element-invisible">(active tab)</span></a></li>
<li><a href="/node/1225/backlinks?language=en">What links here</a></li>
</ul></div>                  

        <div class="region region-content">
    <div id="block-system-main" class="block block-system">

    
  <div class="content">
    <article id="node-1225" class="node node-article node-full clearfix" about="/bayesian-based-mt-saphir-rainfall?language=en" typeof="sioc:Item foaf:Document" role="article">



      <span property="dc:title" content="Bayesian based MT-SAPHIR rainfall" class="rdf-meta element-hidden"></span><span property="sioc:num_replies" content="0" datatype="xsd:integer" class="rdf-meta element-hidden"></span>

  

  <div class="content clearfix">

    <div class="field field-name-field-image field-type-image field-label-hidden"><div class="field-items"><div class="field-item even" rel="og:image rdfs:seeAlso" resource="https://www.mosdac.gov.in/sites/default/files/styles/medium/public/field/image/saphir_rain.jpg?itok=HGUH8nsw"><img typeof="foaf:Image" src="https://www.mosdac.gov.in/sites/default/files/styles/medium/public/field/image/saphir_rain.jpg?itok=HGUH8nsw" width="220" height="110" alt="Rainfall" /></div></div></div><div class="field field-name-body field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even" property="content:encoded"><div style="text-align: justify;">Megha- Tropiques (MT) is a joint Indo-French collaborative satellite mission, which is launched on 12 October 2011. The main objective of MT is to get more understanding on convective system, energy exchange and water cycle in the tropical region. It is equipped with Microwave Analysis and Detection of Rain and Atmospheric Structures (MADRAS) (not in operational), Scanner for Radiation Budget, Radio Occultation Sensor for Atmosphere and  Sondeur Atmospherique du Profil d’Humidite Intertropical par Radiometrie (SAPHIR). SAPHIR provides clear sky atmospheric humidity profiles at 6-channels near 183.31GHz water vapour resonance. The observations of SAPHIR  provides an opportunity to estimate rainfall using 183.31GHz channels.  A Bayesian based rainfall retrieval technique is developed using SAPHIR channel-6 (183.31±11GHz) brightness temperature observations. Estimated rainfall has been validated with IMERG and DPR products during Jan-Dec 2017. The global distribution of rainfall patterns are captured well by the estimation. </div>
<p> </p>
<div id="accordion">
<h3><span style="color: #0000ff;">Data Access</span></h3>
<div><a href="/opendata/bayesian_saphir_rainfall/">Click Here</a> to access the Science Products. Request to use MOSDAC Single Sign On user credentials to download the data.</div>
<h3><span style="color: #0000ff;">Data Version</span></h3>
<div>
<ul style="list-style: none;">
<li>Version 1.1 (beta)</li>
</ul>
</div>
<h3><span style="color: #0000ff;">Data Sources</span></h3>
<div>
<ul style="list-style: none;">
<li>SAPHIR Level 1A TB data</li>
</ul>
</div>
<h3><span style="color: #0000ff;">Processing Steps</span></h3>
<div>
<ul style="list-style: none;">
<li>SAPHIR Level-1 brightness temperature of channel-6 (Tb6) and spatial variability of Tb6 (Std-tb6) within ±3 pixels (~30km at nadir and ~60km off nadir) is calculated.<br />Bayesian algorithm is trained using GPM-IMERG half hourly rainfall Bayesian approach is applied to estimate rainfall from SAPHIR sounder observations.</li>
</ul>
</div>
<h3><span style="color: #0000ff;">References</span></h3>
<div>
<ul style="list-style: none;">
<li>Kummerow, C.D., W. S. Olson, and L. Giglio, A simplified scheme for obtaining precipitation and vertical hydrometeor profiles from passive microwave sensors, IEEE Trans. Geosci. Remote Sens., vol. 34, no. 5, pp. 1213–1232, Sep. 1996.<br />Pierdicca, N., F. S. Marzano, G. D’Auria, P. Basili, P. Ciotti, and A. Mugnai, Precipitation retrieval from spaceborne microwave radiometers using maximum a posteriori probability estimation, IEEE Trans. Geosci. Remote Sens., vol. 34, no. 4, pp. 831–846, Jul. 1996.<br /> Olson, W.S., C. D. Kummerow, G. M. Heymsfield, and L. Giglio, A method for combined passive-active microwave retrievals of cloud and precipitation parameters, J. Appl. Meteorol., vol. 35, pp. 1763–1789, 1996.<br />Marzano, F.S., A. Mugnai, G. Panegrossi, N. Pierdicca, E. A. Smith, and J. Turk, Bayesian estimation of precipitating cloud parameters from combined measurements of spaceborne microwave radiometer and radar, IEEE Trans. Geosci. Remote Sens., vol. 37, no. 1, pp. 596–613, Jan. 1999.<br />Viltard, N., C. Burlaud, and C. D. Kummerow, Rain retrieval from TMI brightness temperature measurements using a TRMM PR–based database. J. Appl. Meteor. Climatol, 45, 455–466, doi:10.1175/JAM2346.1, 2006.<br />Gopalan, K., N.-Y. Wang, R. Ferraro, and C. Liu,  Status of the TRMM 2A12 land precipitation algorithm. J. Atmos. Oceanic Technol., 27, 1343–1354, doi:10.1175/2010JTECHA1454.1, 2010.</li>
</ul>
</div>
<h3><span style="color: #0000ff;">Derivation Techniques and Algorithm</span></h3>
<div>
<ul style="list-style: none;">
<li>User should refer report “Rainfall Estimation from Megha-Tropiques Microwave Sounder-SAPHIR using Bayesian Approach” for complete reference to the algorithm.</li>
</ul>
</div>
<h3><span style="color: #0000ff;">Limitations</span></h3>
<div>
<ul style="list-style: none;">
<li>Rainfall estimates are not provided in the 3 outermost scan positions of the SAPHIR scan.</li>
</ul>
</div>
<h3><span style="color: #0000ff;">Known problems with data</span></h3>
<div>
<ul style="list-style: none;">
<li>No known issues at this time.</li>
</ul>
</div>
<h3><span style="color: #0000ff;">File Naming Convention</span></h3>
<div>
<ul style="list-style: none;">
<ul style="list-style: none;">HDF5 file:</ul>
</ul>
<p>
</p><ul style="list-style: none;">
<ul style="list-style: none;">MTSAPS__VVV_*_YYYY_MM_DD_*.Bayesian_RR.h5</ul>
</ul>
<p>
</p><ul style="list-style: none;">
<ul style="list-style: none;">VVV is the Level 1 version number</ul>
</ul>
<p>
</p><ul style="list-style: none;">YYYY is the year, MM is the month and DD is the date of the orbit.</ul>
</div>
<h3><span style="color: #0000ff;">MetaData</span></h3>
<div>
<table style="margin-left: 10px;" border="0" cellpadding="5">
<tbody>
<tr style="background-color: #095cb1; color: white;">
<td>Sr. No</td>
<td>Core Metadata Elements</td>
<td>Definition</td>
</tr>
<tr>
<td>1</td>
<td>Metadata language</td>
<td>English</td>
</tr>
<tr>
<td>2</td>
<td>Metadata Contact</td>
<td>MOSDAC</td>
</tr>
<tr>
<td>3</td>
<td>Metadata date</td>
<td>June 2018</td>
</tr>
<tr>
<td>4</td>
<td>Data Lineage or Quality</td>
<td>Rain Rate</td>
</tr>
<tr>
<td>5</td>
<td>Title</td>
<td>Bayesian based MT-SAPHIR rainfall</td>
</tr>
<tr>
<td>6</td>
<td>Abstract</td>
<td>Megha- Tropiques (MT) is a joint Indo-French collaborative satellite mission, which is launched on 12 October 2011. The main objective of MT is to get more understanding on convective system, energy exchange and water cycle in the tropical region. It is equipped with Microwave Analysis and Detection of Rain and Atmospheric Structures (MADRAS) (not in operational), Scanner for Radiation Budget and Radio Occultation Sensor for Atmosphere and  Sondeur Atmospherique du Profil d’Humidite Intertropical par Radiometrie (SAPHIR). SAPHIR provides clear sky atmospheric humidity profiles at 6-channels near 183.31GHz water vapour resonance. The observations of SAPHIR  provides an opportunity to estimate rainfall using 183.31GHz channels.  A Bayesian based rainfall retrieval technique is developed using SAPHIR channel-6 (183.31±11GHz) brightness temperature observations. Estimated rainfall has been validated with IMERG and DPR products during Jan-Dec 2017. The global distribution of rainfall patterns are captured well by the estimation. </td>
</tr>
<tr>
<td>7</td>
<td>Dataset Contact</td>
<td>Neerja Sharma and Kaushik Gopalan, GRD/AOSG/EPSA, Space Applications Centre (ISRO), Ahmedabad, 380015, <a href="mailto:kaushikg@sac.isro.gov.in">kaushikg@sac.isro.gov.in</a></td>
</tr>
<tr>
<td>8</td>
<td>Update Frequency</td>
<td>January 2017 to May 2018 have been processed. Data will be updated daily with ~24 hours lag.</td>
</tr>
<tr>
<td>9</td>
<td>Access Rights or Restriction</td>
<td>Open Access</td>
</tr>
<tr>
<td>10</td>
<td>Spatial Resolution</td>
<td>Data is provided at native spatial resolution of the SAPHIR instrument.</td>
</tr>
<tr>
<td>11</td>
<td>Language</td>
<td>English</td>
</tr>
<tr>
<td>12</td>
<td>Topic Category</td>
<td>Rainfall</td>
</tr>
<tr>
<td>13</td>
<td>Keywords</td>
<td>Microwave sounder, Bayesian technique, rainfall</td>
</tr>
<tr>
<td>14</td>
<td>Date or period</td>
<td>From January 2017 onwards.</td>
</tr>
<tr>
<td>15</td>
<td>Responsible Party</td>
<td>Neerja Sharma and Kaushik Gopalan,GRD/AOGG/ EPSA, Space Applications Centre (ISRO), Ahmedabad-380015, India</td>
</tr>
<tr>
<td>16</td>
<td>Organization</td>
<td>Space Applications Centre (ISRO), Ahmedabad, India</td>
</tr>
<tr>
<td>16a</td>
<td>Org. role</td>
<td>Rainfall retrieval from MT-SAPHIR observations</td>
</tr>
<tr>
<td>16b</td>
<td>Individual name</td>
<td>
<p>Neerja Sharma, GRD/AOSG/EPSA, SAC(ISRO), Ahmedabad-380015, India. Ph:+91 79 26916115. Email:<a href="mailto:neerjasharma@sac.isro.gov.in">neerjasharma@sac.isro.gov.in</a></p>
<p>Kaushik Gopalan, GRD/AOSG/EPSA, SAC (ISRO), Ahmedabad-380015, India. Ph: +91 79 2691 6110. Email: <a href="mailto:kaushikg@sac.isro.gov.in">kaushikg@sac.isro.gov.in</a></p>
</td>
</tr>
<tr>
<td>16c</td>
<td>Position</td>
<td>Scientist/Engineer, GRD/AOSG/EPSA, SAC (ISRO), Ahmedabad-380015</td>
</tr>
<tr>
<td>16d</td>
<td>Vertical Extent (minimumValue, maximumValue, unitOfMeasure, vertical datum)</td>
<td>NA</td>
</tr>
<tr>
<td>17</td>
<td>Geographic Extent</td>
<td>Tropical region (28S to 28N)</td>
</tr>
<tr>
<td>18</td>
<td>Geographic name, geographic Identifier</td>
<td>lat_min: 28S,  lat_max: 28N, lon_min: 0, lon_max: 360</td>
</tr>
<tr>
<td>19</td>
<td>Bounding box</td>
<td>lat_min: 28S, lat_max: 28N, lon_min: 0, lon_max: 360</td>
</tr>
<tr>
<td>20</td>
<td>Temporal Extent</td>
<td>January 2017 onwards</td>
</tr>
<tr>
<td>21</td>
<td>Access Rights or Restrictions</td>
<td>Open Access</td>
</tr>
<tr>
<td>22</td>
<td>Distribution Information</td>
<td>Online download of data files in HDF5 format</td>
</tr>
<tr>
<td>23</td>
<td>Processing Level</td>
<td>Level 2 (Data product derived from MT SAPHIR)</td>
</tr>
<tr>
<td>24</td>
<td>Reference System</td>
<td>Datum: WGS84</td>
</tr>
</tbody>
</table>
</div>
</div>
<p> </p>
</div></div></div><div class="field field-name-field-tags field-type-taxonomy-term-reference field-label-above clearfix"><h3 class="field-label">Tags: </h3><ul class="links"><li class="taxonomy-term-reference-0" rel="dc:subject"><a href="/tags/opendata?language=en" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">Opendata</a></li><li class="taxonomy-term-reference-1" rel="dc:subject"><a href="/tags/atmosphere?language=en" typeof="skos:Concept" property="rdfs:label skos:prefLabel" datatype="">Atmosphere</a></li></ul></div>  </div>



  

  

</article>

  </div>
</div>
  </div>
    	</div>

     </div> <!-- /.section, /#content -->



    

    

  </div></div> <!-- /#main, /#main-wrapper -->



  

  <div id="footer-wrapper"><div class="section">



          <div id="footer-columns" class="clearfix">

          <div class="region region-footer-firstcolumn">
    <div id="block-search-form" class="block block-search">

    <h2>Search</h2>
  
  <div class="content">
    <form action="/bayesian-based-mt-saphir-rainfall?language=en" method="post" id="search-block-form" accept-charset="UTF-8"><div><div class="container-inline">
    <div class="form-item form-type-textfield form-item-search-block-form">
  <label class="element-invisible" for="edit-search-block-form--2">Search </label>
 <input title="Enter the terms you wish to search for." type="text" id="edit-search-block-form--2" name="search_block_form" value="" size="15" maxlength="128" class="form-text" />
</div>
<div class="form-actions form-wrapper" id="edit-actions"><input type="submit" id="edit-submit--2" name="op" value="Search" class="form-submit" /></div><input type="hidden" name="form_build_id" value="form-yx_KB7T6dw_M5-3VaADhfyX_UE6ipviyGMA1oKb8D4s" />
<input type="hidden" name="form_id" value="search_block_form" />
</div>
</div></form>  </div>
</div>
  </div>
          <div class="region region-footer-secondcolumn">
    <div id="block-social-media-links-social-media-links" class="block block-social-media-links">

    <h2>Follow Us</h2>
  
  <div class="content">
    <ul class="social-media-links platforms inline horizontal"><li  class="facebook first"><a href="https://www.facebook.com/mosdac.sac.isro" target="_blank" title="Facebook"><img src="https://www.mosdac.gov.in/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/facebook.png" alt="Facebook icon" /></a></li><li  class="youtube_channel"><a href="http://www.youtube.com/channel/UCDVkai9WIgY2ZgrlF_08Yeg" target="_blank" title="Youtube (Channel)"><img src="https://www.mosdac.gov.in/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/youtube.png" alt="Youtube (Channel) icon" /></a></li><li  class="rss last"><a href="https://www.mosdac.gov.in/?language=enrss.xml" target="_blank" title="RSS"><img src="https://www.mosdac.gov.in/sites/all/modules/social_media_links/libraries/elegantthemes/PNG/rss.png" alt="RSS icon" /></a></li></ul>  </div>
</div>
  </div>
          <div class="region region-footer-thirdcolumn">
    <div id="block-block-6" class="block block-block">

    
  <div class="content">
    <p style="text-align: center;"><span style="color: #ffffff;">Website owned and maintained by MOSDAC, Space Applications Centre, Indian Space Research Organisation, Govt. of INDIA.</span></p>
  </div>
</div>
  </div>
          <div class="region region-footer-fourthcolumn">
    <div id="block-block-10" class="block block-block">

    
  <div class="content">
    <ul class="social-media-links platforms inline horizontal">
<li><a title="Quality Certificate" href="/docs/STQC.pdf" target="_blank"><img style="display: block; margin-left: auto; margin-right: auto;" src="/docs/cqw_logo.gif" alt="CQW LOGO" /></a></li>
</ul>
  </div>
</div>
  </div>
      </div> <!-- /#footer-columns -->

    

          <footer id="footer" role="contentinfo" class="clearfix">

          <div class="region region-footer">
    <nav id="block-menu-menu-policies" class="block block-menu" role="navigation">



    

  <div class="content">

    <ul class="menu clearfix"><li class="first leaf"><a href="/mosdac-feedback?language=en" title="">Feedback</a></li>
<li class="leaf"><a href="/about-us?language=en" title="">About Us</a></li>
<li class="leaf"><a href="/contact-us?language=en" title="">Contact Us</a></li>
<li class="leaf"><a href="/copyright-policy?language=en" title="">Copyright Policy</a></li>
<li class="leaf"><a href="/data-access-policy?language=en" title="">Data Access Policy</a></li>
<li class="leaf"><a href="/hyperlink-policy?language=en" title="">Hyperlink Policy</a></li>
<li class="leaf"><a href="/privacy-policy?language=en" title="">Privacy Policy</a></li>
<li class="leaf"><a href="/website-policies?language=en" title="">Website Policies</a></li>
<li class="leaf"><a href="/terms-conditions?language=en" title="">Terms &amp; Conditions</a></li>
<li class="last leaf"><a href="/faq-page?language=en" title="">FAQs</a></li>
</ul>  </div>

</nav>

<div id="block-views-icons-footer-block" class="block block-views">

    
  <div class="content">
    <div class="view view-icons-footer view-id-icons_footer view-display-id-block view-dom-id-68fb6ac9d422dc06b3f7d258a92dab4d">
        
  
  
      <div class="view-content">
      <div class="views-fluid-grid">
    <ul class="views-fluid-grid-list views-fluid-grid-items-width-150">
          <li class="views-fluid-grid-inline views-fluid-grid-item views-row views-row-1 views-row-odd views-row-first">  
  <div class="views-field views-field-field-icon">        <div class="field-content"><a href="http://www.isro.gov.in"><img typeof="foaf:Image" src="https://www.mosdac.gov.in/sites/default/files/styles/thumbnail/public/logo-transparent.png?itok=IUS20l-w" width="100" height="90" alt="ISRO" /></a></div>  </div></li>
          <li class="views-fluid-grid-inline views-fluid-grid-item views-row views-row-2 views-row-even">  
  <div class="views-field views-field-field-icon">        <div class="field-content"><a href="http://www.sac.gov.in"><img typeof="foaf:Image" src="https://www.mosdac.gov.in/sites/default/files/styles/thumbnail/public/saclogo.png?itok=_Jv4AuIn" width="100" height="66" alt="Space Applications Center" /></a></div>  </div></li>
          <li class="views-fluid-grid-inline views-fluid-grid-item views-row views-row-3 views-row-odd">  
  <div class="views-field views-field-field-icon">        <div class="field-content"><a href="http://www.india.gov.in"><img typeof="foaf:Image" src="https://www.mosdac.gov.in/sites/default/files/styles/thumbnail/public/india-gov_0.png?itok=yssAPH3m" width="100" height="75" alt="NationalPortal" /></a></div>  </div></li>
          <li class="views-fluid-grid-inline views-fluid-grid-item views-row views-row-4 views-row-even">  
  <div class="views-field views-field-field-icon">        <div class="field-content"><a href="http://mygov.in/"><img typeof="foaf:Image" src="https://www.mosdac.gov.in/sites/default/files/styles/thumbnail/public/mygov_0.png?itok=Po-dzdT3" width="100" height="75" alt="MyGov" /></a></div>  </div></li>
          <li class="views-fluid-grid-inline views-fluid-grid-item views-row views-row-5 views-row-odd">  
  <div class="views-field views-field-field-icon">        <div class="field-content"><a href="http://www.digitalindia.gov.in/"><img typeof="foaf:Image" src="https://www.mosdac.gov.in/sites/default/files/styles/thumbnail/public/digital-india_0.png?itok=ntlP7atE" width="100" height="75" alt="DigitalIndia" /></a></div>  </div></li>
          <li class="views-fluid-grid-inline views-fluid-grid-item views-row views-row-6 views-row-even views-row-last">  
  <div class="views-field views-field-field-icon">        <div class="field-content"><a href="http://data.gov.in"><img typeof="foaf:Image" src="https://www.mosdac.gov.in/sites/default/files/styles/thumbnail/public/data-gov.png?itok=qYA78FgB" width="100" height="75" alt="DataPortal" /></a></div>  </div></li>
          </ul>
</div>    </div>
  
  
  
  
  
  
</div>  </div>
</div>
<div id="block-block-11" class="block block-block">

    
  <div class="content">
    <p>"Ver 3.0; Last reviewed and updated on
13 Mar, 2025&amp; Served By:
Web-Srv-Pri</p>  </div>
</div>
  </div>
		<div id="footer-line">

	<!--Ver 3.0; Last reviewed and updated on 13 Mar, 2025 & Served By: Web-Srv-Pri -->

	</div>

      </footer> <!-- /#footer -->

    

  </div></div> <!-- /.section, /#footer-wrapper -->



</div></div> <!-- /#page, /#page-wrapper -->

<!-- Piwik -->

<!--

<script type="text/javascript">

  var _paq = _paq || [];

  _paq.push(["setDomains", ["*.mosdac.gov.in"]]);

  _paq.push(['trackPageView']);

  _paq.push(['enableLinkTracking']);

  (function() {

    var u="//mosdac.gov.in/visit/";

    _paq.push(['setTrackerUrl', u+'piwik.php']);

    _paq.push(['setSiteId', 1]);

    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];

    g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);

  })();

</script> -->

<!-- End Piwik Code -->



<!-- Matomo -->

<script>

  var _paq = window._paq = window._paq || [];

  /* tracker methods like "setCustomDimension" should be called before "trackPageView" */

  _paq.push(['trackPageView']);

  _paq.push(['enableLinkTracking']);

  (function() {

    var u="//mosdac.gov.in/matomo/";

    _paq.push(['setTrackerUrl', u+'matomo.php']);

    _paq.push(['setSiteId', '1']);

    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];

    g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);

  })();

</script>

<!-- End Matomo Code -->



  </body>

</html>


"""
soup = BeautifulSoup(html_data, "html.parser")

# Extract text
text = soup.get_text(separator=" ", strip=True)
print(text)  # Output: "Sample Title This is a paragraph."