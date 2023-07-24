'use strict';

var cibFilezilla = ["32 32", "<path d='M32.005 2.479v-1.411c-0.287 0-0.563-0.115-0.76-0.313-0.199-0.197-0.313-0.473-0.313-0.76h-1.411c-0.032 0.593-0.537 1.052-1.125 1.021-0.552-0.027-0.995-0.469-1.021-1.021h-1.416c-0.037 0.593-0.543 1.047-1.136 1.011-0.541-0.036-0.973-0.469-1.005-1.011h-1.411c-0.032 0.593-0.537 1.052-1.131 1.021-0.547-0.027-0.989-0.469-1.021-1.021h-1.411c-0.032 0.593-0.532 1.052-1.125 1.021-0.552-0.027-0.989-0.469-1.021-1.021h-1.411c-0.036 0.593-0.541 1.047-1.136 1.011-0.541-0.036-0.973-0.469-1.011-1.011h-1.411c-0.016 0.593-0.511 1.057-1.099 1.036-0.563-0.020-1.016-0.473-1.037-1.036h-1.411c-0.032 0.593-0.537 1.052-1.131 1.021-0.547-0.027-0.989-0.469-1.016-1.021h-1.411c-0.027 0.593-0.521 1.057-1.109 1.036-0.563-0.020-1.016-0.473-1.037-1.036h-1.411c0 0.287-0.115 0.563-0.313 0.76-0.203 0.199-0.473 0.313-0.76 0.313v1.411c0.593 0.027 1.052 0.521 1.032 1.109-0.016 0.563-0.469 1.016-1.032 1.037v1.411c0.593 0.021 1.052 0.516 1.032 1.109-0.016 0.563-0.469 1.016-1.032 1.037v1.411c0.593 0 1.073 0.48 1.073 1.073 0 0.588-0.48 1.073-1.073 1.073v1.411c0.593 0 1.073 0.48 1.073 1.068 0 0.593-0.48 1.073-1.073 1.073v1.416c0.593 0.021 1.052 0.516 1.032 1.109-0.016 0.563-0.469 1.011-1.032 1.032v1.416c0.593 0 1.073 0.48 1.073 1.068 0 0.593-0.48 1.073-1.073 1.073v1.416c0.593 0.021 1.052 0.516 1.032 1.104-0.016 0.563-0.469 1.021-1.032 1.037v1.411c0.593 0 1.073 0.48 1.073 1.079 0 0.588-0.48 1.068-1.073 1.068v1.416c0.589 0 1.073 0.479 1.073 1.068h1.411c0.037-0.589 0.548-1.041 1.141-1.005 0.541 0.036 0.968 0.464 1.005 1.005h1.411c0.032-0.589 0.537-1.047 1.125-1.016 0.552 0.027 0.995 0.469 1.021 1.016h1.411c0.032-0.589 0.537-1.047 1.125-1.016 0.552 0.027 0.995 0.469 1.021 1.016h1.411c0.027-0.589 0.521-1.052 1.109-1.032 0.563 0.021 1.016 0.475 1.037 1.032h1.411c0.032-0.589 0.537-1.047 1.131-1.016 0.547 0.027 0.989 0.469 1.016 1.016h1.411c0.032-0.589 0.537-1.047 1.131-1.016 0.547 0.027 0.989 0.469 1.016 1.016h1.411c0.032-0.589 0.537-1.047 1.131-1.016 0.552 0.027 0.989 0.469 1.020 1.016h1.412c0.021-0.589 0.516-1.052 1.109-1.032 0.563 0.021 1.016 0.475 1.032 1.032h1.405c0-0.281 0.115-0.557 0.313-0.755 0.197-0.199 0.473-0.313 0.76-0.313v-1.416c-0.593-0.037-1.041-0.543-1.011-1.136 0.036-0.541 0.469-0.973 1.011-1.005v-1.411c-0.593-0.032-1.052-0.537-1.021-1.125 0.027-0.552 0.469-0.995 1.021-1.021v-1.416c-0.593-0.037-1.041-0.547-1.011-1.136 0.036-0.541 0.469-0.973 1.011-1.005v-1.416c-0.593-0.027-1.052-0.532-1.021-1.125 0.027-0.547 0.469-0.989 1.021-1.021v-1.405c-0.593-0.037-1.041-0.548-1.011-1.141 0.036-0.541 0.469-0.973 1.011-1.005v-1.411c-0.593-0.032-1.052-0.537-1.021-1.125 0.027-0.552 0.469-0.995 1.021-1.021v-1.411c-0.593-0.037-1.041-0.547-1.011-1.141 0.036-0.536 0.469-0.968 1.011-1.005v-1.411c-0.593-0.032-1.052-0.537-1.021-1.125 0.027-0.552 0.469-0.989 1.021-1.021zM26.579 15.599l-8.537 8.303c0.771 0.12 1.521 0.296 2.323 0.296 1.953 0 4.199-0.593 5.715-1.219l-0.776 3.661c-2.235 1.073-3.605 1.163-4.939 1.163-1.463 0-2.859-0.48-4.285-0.48-0.808 0-1.969 0.063-2.683 0.537l-1.547-2.74 8.807-8.719h-10.135l-1.933 9.072h-4.228l4.405-20.771h13.989l-0.895 4.193h-9.729l-0.833 3.901h15.968z'/>"];

exports.cibFilezilla = cibFilezilla;
//# sourceMappingURL=cib-filezilla.js.map
