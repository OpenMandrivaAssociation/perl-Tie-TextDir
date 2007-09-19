%define module	Tie-TextDir
%define	name	perl-%{module}
%define version 0.06
%define release %mkrel 3

Summary:	%{module} module for perl
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MPL
Group:		Development/Perl
Source0:	http://www.cpan.org/authors/id/KWILLIAMS/%{module}-%{version}.tar.bz2
Url:		http://www.cpan.org/
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	perl
BuildArch:	noarch

%description
%{module} module for perl

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes MANIFEST README
%{_mandir}/*/*
%{perl_vendorlib}/Tie


