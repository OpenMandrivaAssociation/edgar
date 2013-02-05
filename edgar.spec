%define rel 2

Name:		edgar
Summary:	2D Platform Game
Version:	1.06
Release:	1
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
%makeinstall_std

%find_lang %{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
	--remove-category=Application \
	--add-category="AdventureGame" \
	%{buildroot}%{_datadir}/applications/edgar.desktop

rm -rf %{buildroot}%{_datadir}/doc

%files -f %{name}.lang
%doc doc/*
%{_gamesbindir}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*

%files data
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*

