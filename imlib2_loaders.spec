%define name    imlib2_loaders
%define version 1.1.2
%define release %mkrel 0.%{cvsrel}.3

%define cvsrel 20060103

Summary: Additional image loaders for Imlib2
Name: %{name}
Version: %{version}
Release: %{release}
License: Distributable
Group: System/Libraries
Source: %{name}-%{cvsrel}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://www.enlightenment.org/pages/imlib2.html
Buildrequires: imlib2-devel libltdl-devel
Requires: imlib2 

%description
This package contains additional image loaders for Imlib2,
which for some reason (such as license issues, Imlib2 is BSD licensed, see 
README inside) are not distributed with Imlib2 directly.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %name

%build

./autogen.sh

%make

%install

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root) 
%doc AUTHORS COPYING* 
%_libdir/imlib2/loaders/*
