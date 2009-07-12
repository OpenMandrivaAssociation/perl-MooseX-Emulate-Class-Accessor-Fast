%define upstream_name    MooseX-Emulate-Class-Accessor-Fast
%define upstream_version 0.00902

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Emulate Class::Accessor::Fast behavior using Moose attributes
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Moose)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(namespace::clean)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module attempts to hijack the Class::Accessor::Fast manpage in %INC
and replace it with the MooseX::Emulate::Class::Accessor::Fast manpage.
Make sure it is loaded before the classes you have that use
<Class::Accessor::Fast>. It is meant as a tool to help you migrate your
project from the Class::Accessor::Fast manpage, to the
MooseX::Emulate::Class::Accessor::Fast manpage and ultimately, to the Moose
manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

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


