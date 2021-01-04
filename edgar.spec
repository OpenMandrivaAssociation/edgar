Name:		edgar
Summary:	2D Platform Game
Version:	1.34
Release:	1
URL:		https://www.parallelrealities.co.uk/games/edgar/
Source0:	https://github.com/riksweeney/edgar/releases/download/%{version}/%{name}-%{version}-1.tar.gz
Group:		Games/Adventure
License:	GPLv2

BuildRequires:	gettext
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(SDL2_ttf)
BuildRequires:	pkgconfig(zlib)

Requires:	%{name}-data >= %{version}

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
%autosetup -p1

%build
%set_build_flags
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%{_gamesbindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_docdir}/%{name}/
%{_mandir}/man6/%{name}.6*

%files data
%{_gamesdatadir}/%{name}/
