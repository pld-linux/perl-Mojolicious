#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Mojolicious
%include	/usr/lib/rpm/macros.perl
Summary:	A next generation web framework for the Perl programming language
Name:		perl-Mojolicious
Version:	6.0
Release:	1
License:	artistic_2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mojolicious/%{pdir}-%{version}.tar.gz
# Source0-md5:	badb7f7b4db8e9ef427d4d1178f15b6c
URL:		https://metacpan.org/release/Mojolicious
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A next generation web framework for the Perl programming language.

%package -n perl-Mojo
Summary:	Duct tape for the HTML5 web!
Group:		Development/Languages/Perl

%description -n perl-Mojo
Duct tape for the HTML5 web!

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/hypnotoad
%attr(755,root,root) %{_bindir}/mojo
%attr(755,root,root) %{_bindir}/morbo
%{perl_vendorlib}/Mojo/HelloWorld.pm
%{perl_vendorlib}/Mojolicious.pm
%{perl_vendorlib}/Mojolicious/*.pm
%{perl_vendorlib}/Mojolicious/*.pod
%dir %{perl_vendorlib}/Mojolicious
%dir %{perl_vendorlib}/Mojolicious/Command
%{perl_vendorlib}/Mojolicious/Command/*.pm
%dir %{perl_vendorlib}/Mojolicious/Command/generate
%{perl_vendorlib}/Mojolicious/Command/generate/*.pm
%dir %{perl_vendorlib}/Mojolicious/Guides
%{perl_vendorlib}/Mojolicious/Guides/*.pod
%dir %{perl_vendorlib}/Mojolicious/Plugin
%{perl_vendorlib}/Mojolicious/Plugin/*.pm
%dir %{perl_vendorlib}/Mojolicious/Routes
%{perl_vendorlib}/Mojolicious/Routes/*.pm
%dir %{perl_vendorlib}/Mojolicious/Validator
%{perl_vendorlib}/Mojolicious/Validator/*.pm
%{perl_vendorlib}/Mojolicious/public
%dir %{perl_vendorlib}/Mojolicious/templates
%{perl_vendorlib}/Mojolicious/templates/*.html.ep
%{perl_vendorlib}/Test/Mojo.pm
%{_mandir}/man1/*
%{_mandir}/man3/Mojolicious::*
%{_mandir}/man3/Mojolicious.3*
%{_mandir}/man3/Test::Mojo.3*
%{_examplesdir}/%{name}-%{version}

%files -n perl-Mojo
%defattr(644,root,root,755)
%{perl_vendorlib}/Mojo.pm
%dir %{perl_vendorlib}/Mojo
%{perl_vendorlib}/Mojo/*.pm
%exclude %{perl_vendorlib}/Mojo/HelloWorld.pm
%dir %{perl_vendorlib}/Mojo/Asset
%{perl_vendorlib}/Mojo/Asset/*.pm
%dir %{perl_vendorlib}/Mojo/Content
%{perl_vendorlib}/Mojo/Content/*.pm
%dir %{perl_vendorlib}/Mojo/Cookie
%{perl_vendorlib}/Mojo/Cookie/*.pm
%dir %{perl_vendorlib}/Mojo/DOM
%{perl_vendorlib}/Mojo/DOM/*.pm
%dir %{perl_vendorlib}/Mojo/IOLoop
%{perl_vendorlib}/Mojo/IOLoop/*.pm
#%{perl_vendorlib}/Mojo/IOLoop/certs/server.crt
#%{perl_vendorlib}/Mojo/IOLoop/certs/server.key
%dir %{perl_vendorlib}/Mojo/JSON
%{perl_vendorlib}/Mojo/JSON/*.pm
%dir %{perl_vendorlib}/Mojo/Message
%{perl_vendorlib}/Mojo/Message/*.pm
%dir %{perl_vendorlib}/Mojo/Reactor
%{perl_vendorlib}/Mojo/Reactor/*.pm
%dir %{perl_vendorlib}/Mojo/Server
%{perl_vendorlib}/Mojo/Server/*.pm
%dir %{perl_vendorlib}/Mojo/Transaction
%{perl_vendorlib}/Mojo/Transaction/*.pm
%dir %{perl_vendorlib}/Mojo/UserAgent
%{perl_vendorlib}/Mojo/UserAgent/*.pm
%{perl_vendorlib}/ojo.pm
%{_mandir}/man3/Mojo::*
%{_mandir}/man3/Mojo.3*
%{_mandir}/man3/ojo.3*
