"use strict";(self.webpackChunkemtiazy=self.webpackChunkemtiazy||[]).push([[133],{2133:function(a,t,e){e.r(t),e.d(t,{default:function(){return U}});var n=e(5671),o=e(3144),s=e(136),c=e(7277),r=e(2791),i=(e(3475),e(2089)),l=e(7022),h=e(6600),d=e(4569),m=e.n(d),p=e(703),x=e(3504),f=e(3400),u=e(2392),Z=e(4177),b=e(1644),j=e(6655),g=e(4523),v=e(1324),w=e(4939),k=e(3767),y=e(6944),N=e(4554),L=e(7047),C=e(1918),D=e(890),I=e(184),U=function(a){(0,s.Z)(e,a);var t=(0,c.Z)(e);function e(a){var o;return(0,n.Z)(this,e),(o=t.call(this,a)).logoData=function(){m().get("/api/sitelogo/").then((function(a){o.setState({siteLogo:a.data})})).catch((function(a){return console.log(a)}))},o.contactInfoData=function(){m().get("/api/contactinfo/").then((function(a){o.setState({isLoaded:!0,contactInfo:a.data})})).catch((function(a){return console.log(a)}))},o.state={siteLogo:{},contactInfo:{},isLoaded:!1},o}return(0,o.Z)(e,[{key:"componentDidMount",value:function(){this.logoData(),this.contactInfoData()}},{key:"render",value:function(){var a=this.state,t=a.siteLogo,e=a.contactInfo,n=a.isLoaded;return(0,I.jsx)(p.Z,{component:"nav",className:"navbar-container",children:(0,I.jsx)(i.Z,{collapseOnSelect:!0,expand:"lg",bg:"white",variant:"light",fixed:"top",children:(0,I.jsxs)(l.Z,{fluid:!0,children:[(0,I.jsxs)(i.Z.Brand,{href:"#",children:[(0,I.jsx)("img",{alt:"",src:t.logo,width:"30",height:"30",className:"d-inline-block align-top"})," ",(0,I.jsx)(D.Z,{variant:"span",component:"span",className:"fw-bold fs-5",color:"primary",children:t.name})]}),(0,I.jsx)(i.Z.Toggle,{"aria-controls":"responsive-navbar-nav"}),(0,I.jsxs)(i.Z.Collapse,{id:"responsive-navbar-nav",children:[(0,I.jsx)(h.Z,{className:"me-auto",children:(0,I.jsxs)(k.Z,{direction:"row",children:[(0,I.jsx)(y.Z,{title:"Home",arrow:!0,children:(0,I.jsx)(C.Z,{icon:(0,I.jsx)(u.Z,{}),label:"\u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629",component:"a",clickable:!0,as:x.rU,to:"/",className:"p-3 me-2 mt-1"})}),(0,I.jsx)(y.Z,{title:"About Us",arrow:!0,children:(0,I.jsx)(C.Z,{icon:(0,I.jsx)(Z.Z,{}),label:"\u0639\u0646\u0627",component:"a",clickable:!0,as:x.rU,to:"/about",className:"p-3 me-2 mt-1"})}),(0,I.jsx)(y.Z,{title:"Contact Us",arrow:!0,children:(0,I.jsx)(C.Z,{icon:(0,I.jsx)(b.Z,{}),label:"\u062a\u0648\u0627\u0635\u0644 \u0645\u0639\u0646\u0627",component:"a",clickable:!0,as:x.rU,to:"/contact",className:"p-3 me-2 mt-1"})})]})}),n?(0,I.jsxs)(N.Z,{sx:{pt:.5},children:[e.facebook?(0,I.jsx)(f.Z,{color:"primary",href:e.facebook,target:"_blank","aria-label":"Facebook",className:"ms-2 btn-nav-contact",children:(0,I.jsx)(j.Z,{})}):"",e.twitter?(0,I.jsx)(f.Z,{color:"primary",href:e.twitter,target:"_blank","aria-label":"Twitter",className:"ms-2 btn-nav-contact",children:(0,I.jsx)(g.Z,{})}):"",e.whatsapp?(0,I.jsx)(f.Z,{color:"primary",href:e.whatsapp,target:"_blank","aria-label":"Whatsapp",className:"ms-2 btn-nav-contact",children:(0,I.jsx)(v.Z,{})}):"",e.phone?(0,I.jsx)(f.Z,{color:"primary",href:"tel:"+e.phone,"aria-label":"Phone",className:"ms-2 btn-nav-contact",children:(0,I.jsx)(w.Z,{})}):""]}):(0,I.jsx)(k.Z,{direction:"row",children:Array.from(new Array(4)).map((function(a,t){return(0,I.jsx)(N.Z,{sx:{pt:.5},className:"ms-2",children:(0,I.jsx)(L.Z,{variant:"rectangular",style:{borderRadius:"8px"},width:35,height:35})},t)}))})]})]})})})}}]),e}(r.Component)}}]);
//# sourceMappingURL=133.db122479.chunk.js.map