%define upstream_name    MooseX-Emulate-Class-Accessor-Fast
%define upstream_version 0.00903

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    5
Epoch:      1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Emulate Class::Accessor::Fast behavior using Moose attributes
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Moose)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(namespace::clean)
BuildRequires: perl-devel
BuildArch: noarch

%description
This module attempts to hijack the Class::Accessor::Fast manpage in INC
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
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1:0.9.30-2mdv2011.0
+ Revision: 655063
- rebuild for updated spec-helper

* Wed Sep 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.9.30-1mdv2011.0
+ Revision: 443470
- update to 0.00903

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.9.20-1mdv2010.0
+ Revision: 395169
- update to 0.00902

* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.9.0-1mdv2010.0
+ Revision: 381276
- adding epoch: tag to make sure %%perl_convert_version gets priority
- update to 0.90000
- using %%perl_convert_version
- sanitized license field & description fields

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.00802-1mdv2010.0
+ Revision: 376180
- adding missing buildrequires:
- adding missing buildrequires
- import perl-MooseX-Emulate-Class-Accessor-Fast


* Fri May 15 2009 cpan2dist 0.00802-1mdv
- initial mdv release, generated with cpan2dist

