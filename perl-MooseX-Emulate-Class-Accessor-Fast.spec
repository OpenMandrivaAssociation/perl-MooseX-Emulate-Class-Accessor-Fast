
%define realname   MooseX-Emulate-Class-Accessor-Fast
%define version    0.00802
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Emulate Class::Accessor::Fast behavior using Moose attributes
Source:     http://www.cpan.org/modules/by-module/MooseX/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Moose)
BuildRequires: perl(Test::Exception)


BuildArch: noarch

%description
This module attempts to hijack the Class::Accessor::Fast manpage in %INC
and replace it with the MooseX::Emulate::Class::Accessor::Fast manpage.
Make sure it is loaded before the classes you have that use
<Class::Accessor::Fast>. It is meant as a tool to help you migrate your
project from the Class::Accessor::Fast manpage, to the
MooseX::Emulate::Class::Accessor::Fast manpage and ultimately, to the Moose
manpage.





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


