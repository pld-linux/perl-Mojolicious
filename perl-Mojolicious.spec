#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Mojolicious
%include	/usr/lib/rpm/macros.perl
Summary:	A next generation web framework for the Perl programming language
Summary(pl.UTF-8):	Szkielet WWW następnej generacji dla języka programowania Perl
Name:		perl-Mojolicious
Version:	6.01
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mojolicious/%{pdir}-%{version}.tar.gz
# Source0-md5:	851eefadf653afa777d8b2c73cbc0cf5
URL:		http://mojolicio.us/
BuildRequires:	perl-ExtUtils-MakeMaker
%if %{with tests}
BuildRequires:	perl(IO::Socket::IP) >= 0.26
BuildRequires:	perl(Time::Local) >= 1.2
BuildRequires:	perl-Pod-Simple >= 3.09
%endif
BuildRequires:	perl-devel >= 1:5.10.1
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Mojo = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A next generation web framework for the Perl programming language.

%description -l pl.UTF-8
Szkielet WWW następnej generacji dla języka programowania Perl.

%package -n perl-Mojo
Summary:	Duct tape for the HTML5 web!
Summary(pl.UTF-8):	Taśma klejąca dla WWW opartego na HTML5
Group:		Development/Languages/Perl
Requires:	perl(IO::Socket::IP) >= 0.26
Requires:	perl(Time::Local) >= 1.2

%description -n perl-Mojo
Duct tape for the HTML5 web!

%description -n perl-Mojo -l pl.UTF-8
Taśma klejąca dla WWW opartego na HTML5.

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

# deprecated namespace, but used by some external modules
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/MojoX

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
%{_mandir}/man1/hypnotoad.1p*
%{_mandir}/man1/mojo.1p*
%{_mandir}/man1/morbo.1p*
%{_mandir}/man3/Mojolicious*.3pm*
%{_mandir}/man3/Test::Mojo.3pm*
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
%dir %{perl_vendorlib}/MojoX
%{_mandir}/man3/Mojo.3pm*
%{_mandir}/man3/Mojo::*.3pm*
%{_mandir}/man3/ojo.3pm*
