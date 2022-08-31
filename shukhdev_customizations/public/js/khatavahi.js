$(window).on('load', function() {
	var html_data = `
	<li class="nav-item dropdown dropdown-help dropdown-mobile d-none d-lg-block">
	<a class="nav-link" data-toggle="dropdown" href="#" onclick="return false;"> Company Site <span>
		<svg class="icon icon-xs">
			<use href="#icon-small-down"></use>
		</svg>
		</span>
	</a>
	<div class="dropdown-menu dropdown-menu-right"  role="menu">
		<div ></div>
		
		<a class="dropdown-item" href="https://sepl.xplosives.com" > SUKHDEV EXPLOSIVES PRIVATE LIMITED </a>
		<a class="dropdown-item" href="https://sasl.xplosives.com" > SCHLUMBERGER ASIA SERVICES LIMITED </a>
		<a class="dropdown-item" href="https://aesllp.xplosives.com" > ADVANCE ENERGY SERVICES LLP </a>
		<a class="dropdown-item" href="https://pc.xplosives.com" > POOJA CHEMICALS </a>
		<a class="dropdown-item" href="https://wotmel.xplosives.com" > WEATHERFORD OIL TOOL M. E. LIMITED </a>
		<a class="dropdown-item" href="https://hls.xplosives.com" > HLS ASIA LIMITED </a>
		<a class="dropdown-item" href="https://expro.xplosives.com" > EXPRO NORTH SEA LIMITED </a>
		<a class="dropdown-item" href="https://mmf.xplosives.com" > MANSUKHLAL MOHANLAL FALDU </a>
		<a class="dropdown-item" href="https://mmfhuf.xplosives.com" > MANSUKHLAL MOHANLAL FALDU (HUF) </a>
		<a class="dropdown-item" href="https://smf.xplosives.com" > SAROJBEN MANSUKHLAL FALDU </a>
		<a class="dropdown-item" href="https://prm.xplosives.com" > PRAMIT RASIKLAL MAKADIYA </a>
		<a class="dropdown-item" href="https://prmhuf.xplosives.com"> PRAMIT RASIKLAL MAKADIYA (HUF) </a>
		<a class="dropdown-item" href="https://ppm.xplosives.com" > PUJA PRAMIT MAKADIYA </a>
		<a class="dropdown-item" href="https://hfcl.xplosives.com"> HFCL LIMITED </a>
		<a class="dropdown-item" href="https://stillp.xplosives.com" > SUKHDEV TECHNO INDIA LLP </a>
		<a class="dropdown-item" href="https://sspl.xplosives.com" > SCHLUMBERGER SOLUTIONS PRIVATE LIMITED </a>
	</li>`

    frappe.after_ajax(function () {
        $(html_data).insertAfter("#navbar-breadcrumbs")
    })
})
