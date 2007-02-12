Summary:	An ncurses-based XMMS frontend
Summary(pl.UTF-8):   Oparty o ncurses system sterowania XMMS-em
Name:		ncxmms
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://mrg.risp.pl/dl/%{name}-%{version}.tar.bz2
# Source0-md5:	0a784a748de0d5a8bb97b45f93015df7
Patch0:		%{name}-pld.patch
BuildRequires:	glib-devel
BuildRequires:	ncurses-devel
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NCXmms is an XMMS frontend based on ncurses. Feature highlights
include its ability to control XMMS from a text environment using
comfortable menu library widgets. It can also quickly find items in
the playlist after the user enters part of the name.

%description -l pl.UTF-8
NCXmms jest interfejsem sterowania XMMS-em opartym na bibliotece
ncurses. Jego główne cechy to możliwość kontrolowania XMMS-a ze
środowiska tekstowego, używając wygodnego systemu menu. Można także
szybko wyszukiwać elementy listy odtwarzania poprzez wpisanie części
jego nazwy.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
