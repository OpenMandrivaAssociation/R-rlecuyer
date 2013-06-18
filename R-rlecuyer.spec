%global packname  rlecuyer
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.3_3
Release:          2
Summary:          R interface to RNG with multiple streams
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-3.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

%description
Provides an interface to the C implementation of the random number
generator with multiple independent streams developed by L'Ecuyer et al
(2002). The main purpose of this package is to enable the use of this
random number generator in parallel R applications.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3_3-1
+ Revision: 774953
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3_2-1
+ Revision: 774628
- Import R-rlecuyer
- Import R-rlecuyer

