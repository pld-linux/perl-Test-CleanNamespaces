#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Test
%define		pnam	CleanNamespaces
Summary:	Test::CleanNamespaces - Check for uncleaned imports
Summary(pl.UTF-8):	Test::CleanNamespace - sprawdzanie zanieczyszczonych importów
Name:		perl-Test-CleanNamespaces
Version:	0.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0ddfb7e5f11ddfb9498cb500c7616fb8
URL:		https://metacpan.org/dist/Test-CleanNamespaces
BuildRequires:	perl-CPAN-Meta-Requirements >= 2.120_620
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Package-Stash >= 0.14
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Sub-Identify
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Test-Tester
BuildRequires:	perl-Test-Warnings >= 0.009
BuildRequires:	perl-namespace-clean
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module lets you check your module's namespaces for imported
functions you might have forgotten to remove with namespace::autoclean
or namespace::clean and are therefore available to be called as
methods, which usually isn't want you want.

%description -l pl.UTF-8
Ten moduł pozwala sprawdzić przestrzenie nazw modułu, czy nie
zapomniano z nich usunąć zaimportowanych funkcji przy użyciu
namespace::autoclean lub namespace::clean, przez co mogłyby być
dostępne jako metody, co jest zwykle niepożądane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/Test/CleanNamespaces.pm
%{_mandir}/man3/Test::CleanNamespaces.3pm*
