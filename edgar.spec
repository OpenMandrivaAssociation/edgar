%define rel 2

Name:		edgar
Summary:	2D Platform Game
Version:	1.01
Release:	%mkrel 1
Source:		%{name}-%{version}-%{rel}.tar.gz
Url:		http://www.parallelrealities.co.uk/projects/edgar.php
Group:		Games/Adventure
License:	GPLv2
Requires:	%{name}-data = %{version}
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	zlib-devel
BuildRequires:	desktop-file-utils

%description
The Legend of Edgar. When his father fails to return home after venturing out
one stormy night, Edgar sets off on a quest to rescue him.

%package data
Group:		Games/Arcade
License:	GPLv2
BuildArch:	noarch
Summary:	The Legend of Edgar level set
Requires:	%{name} = %{version}

%description data
The Legend of Edgar. When his father fails to return home after venturing
out one stormy night, Edgar sets off on a quest to rescue him.

This package contains official level set for Edgar.

%prep
%setup -q

%build
%make VERSION=%{version} RELEASE=%{rel}

%install
%__rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
	--remove-category=Application \
	--add-category="AdventureGame" \
	%{buildroot}%{_datadir}/applications/edgar.desktop

%__rm -rf %{buildroot}%{_datadir}/doc

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%doc doc/*
%{_gamesbindir}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*

%files data
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*



%changelog
* Wed May 23 2012 Andrey Bondrov <abondrov@mandriva.org> 1.01-1mdv2011.0
+ Revision: 800241
- New version 1.01

* Tue Apr 24 2012 Andrey Bondrov <abondrov@mandriva.org> 1.00-1
+ Revision: 793103
- New version 1.00

* Fri Apr 06 2012 Andrey Bondrov <abondrov@mandriva.org> 0.99-1
+ Revision: 789577
- New version 0.99-1

* Tue Mar 06 2012 Andrey Bondrov <abondrov@mandriva.org> 0.98-1
+ Revision: 782360
- New version 0.98-2

* Fri Feb 10 2012 Andrey Bondrov <abondrov@mandriva.org> 0.97-1
+ Revision: 772419
- New version 0.97

* Sun Jan 08 2012 Andrey Bondrov <abondrov@mandriva.org> 0.95-1
+ Revision: 758661
- New version 0.95

* Mon Dec 12 2011 Andrey Bondrov <abondrov@mandriva.org> 0.94-1
+ Revision: 740534
- Add patch0 to fix linking
- imported package edgar

