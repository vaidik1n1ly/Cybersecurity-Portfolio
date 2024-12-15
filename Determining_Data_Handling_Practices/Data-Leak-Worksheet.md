<body class="c50 doc-content">
    <h3 class="c39 c16 c41" id="h.u3iqqzpk1ycv"><span class="c24">Data</span><span class="c24 c46">&nbsp;leak
        </span><span class="c24">worksheet</span></h3>
    <hr>
    <p class="c9 c16"><span class="c6"></span></p>
    <p class="c9 c16"><span class="c6"></span></p>
    <p class="c36 c16"><span class="c37">Incident summary:</span><span>&nbsp;</span><span>A sales manager shared access
            to a folder of internal-only documents with their team during a meeting.</span><span class="c6">&nbsp;The
            folder contained files associated with a new product that has not been publicly announced. It also included
            customer analytics and promotional materials. After the meeting, the manager did not revoke access to the
            internal folder, but warned the team to wait for approval before sharing the promotional materials with
            others.</span></p>
    <p class="c0"><span class="c6"></span></p>
    <p class="c36 c16"><span>D</span><span>uring a video call with a business partner</span><span>,
            a</span><span>&nbsp;member of the sales team forgot the warning from their manager. The sales representative
            intended to share a link to the promotional materials so that the business partner could circulate the
            materials to their customers. However, the sales representative accidentally shared a link to the internal
            folder instead. </span><span>Later, the business partner posted the link on their company's social media
            page </span><span>assuming that</span><span>&nbsp;it was the promotional materials.</span></p>
    <p class="c0"><span class="c6"></span></p>
    <table class="c38">
        <tbody>
            <tr class="c17">
                <td class="c18 c44" colspan="1" rowspan="1">
                    <p class="c39"><span class="c5">Control</span></p>
                </td>
                <td class="c8 c44" colspan="3" rowspan="1">
                    <p class="c39"><span class="c21 c40">Least privilege</span></p>
                </td>
            </tr>
            <tr class="c15">
                <td class="c18" colspan="1" rowspan="1">
                    <p class="c39"><span class="c5">Issue(s)</span></p>
                </td>
                <td class="c8" colspan="3" rowspan="1">
                    <p class="c35"><span class="c25">Access to the internal folder was not limited to the sales team and
                            the manager. The business partner should not have been given permission to share the
                            promotional information to social media.</span></p>
                </td>
            </tr>
            <tr class="c4">
                <td class="c18" colspan="1" rowspan="1">
                    <p class="c39"><span class="c37">Review</span></p>
                </td>
                <td class="c8" colspan="3" rowspan="1">
                    <p class="c35"><span class="c14 c12">NIST SP 800-53: AC-6 addresses how an organization can protect
                            their data privacy by implementing least privilege. It also suggests control enhancements to
                            improve the effectiveness of least privilege. </span></p>
                </td>
            </tr>
            <tr class="c30">
                <td class="c18" colspan="1" rowspan="1">
                    <p class="c39"><span class="c5">Recommendation(s)</span></p>
                </td>
                <td class="c8" colspan="3" rowspan="1">
                    <ul class="c26 lst-kix_6hbj96j027hm-0 start">
                        <li class="c1 c43 li-bullet-0"><span class="c14 c12">Restrict access to sensitive resources
                                based on user role. </span></li>
                        <li class="c1 li-bullet-0"><span class="c25">Regularly audit user privileges.</span></li>
                    </ul>
                </td>
            </tr>
            <tr class="c47">
                <td class="c18" colspan="1" rowspan="1">
                    <p class="c39"><span class="c37">Justification</span></p>
                </td>
                <td class="c8" colspan="3" rowspan="1">
                    <p class="c35"><span class="c25">Data leaks can be prevented if shared links to internal files are
                            restricted to employees only. Also, requiring </span><span class="c25">managers and security
                            teams to regularly audit access to team files </span><span class="c25">would help limit the
                            exposure of sensitive information.</span></p>
                </td>
            </tr>
        </tbody>
    </table>
    <h3 class="c16 c27" id="h.ka0u51o5b7wk"><span class="c32">Security plan snapshot</span></h3>
    <p class="c36 c16"><span class="c12">The </span><span>NIST </span><span class="c12">Cybersecurity F</span><span
            class="c6">ramework (CSF) uses a hierarchical, tree-like structure to organize information. From left to
            right, it describes a broad security function, then becomes more specific as it branches out to a category,
            subcategory, and individual security controls.</span></p>
    <p class="c0"><span class="c6"></span></p>
    <table class="c2">
        <tbody>
            <tr class="c42">
                <td class="c49" colspan="1" rowspan="1">
                    <p class="c28"><span class="c21 c33">Function</span></p>
                </td>
                <td class="c19" colspan="1" rowspan="1">
                    <p class="c28"><span class="c33 c21">Category</span></p>
                </td>
                <td class="c29" colspan="1" rowspan="1">
                    <p class="c28"><span class="c33 c21">Subcategory</span></p>
                </td>
                <td class="c11" colspan="1" rowspan="1">
                    <p class="c28"><span class="c33 c21">Reference(s)</span></p>
                </td>
            </tr>
            <tr class="c45">
                <td class="c49 c51" colspan="1" rowspan="1">
                    <p class="c28"><span class="c33 c21">Protect</span></p>
                </td>
                <td class="c19" colspan="1" rowspan="1">
                    <p class="c28"><span class="c12">PR.DS:</span><span class="c12">&nbsp;</span><span
                            class="c12 c14">Data security</span></p>
                </td>
                <td class="c29" colspan="1" rowspan="1">
                    <p class="c48"><span class="c12">PR.DS-5:</span><span class="c12">&nbsp;</span><span
                            class="c14 c12">Protections against data leaks.</span></p>
                </td>
                <td class="c11" colspan="1" rowspan="1">
                    <p class="c28"><span class="c12">NIST SP 800-53:</span><span class="c12">&nbsp;</span><span
                            class="c12">AC-6</span></p>
                </td>
            </tr>
        </tbody>
    </table>
    <p class="c0"><span class="c6"></span></p>
    <p class="c36 c16"><span class="c6">In this example, the implemented controls that are used by the manufacturer to
            protect against data leaks are defined in NIST SP 800-53—a set of guidelines for securing the privacy of
            information systems.</span></p>
    <p class="c0"><span class="c6"></span></p>
    <p class="c36 c16"><span class="c37">Note:</span><span>&nbsp;References are commonly hyperlinked to the guidelines
            or regulations they relate to. This makes it easy to learn more about how a particular control should be
            implemented. It's common to find multiple links to different sources in the references columns.</span></p>
    <hr style="page-break-before:always;display:none;">
    <p class="c0"><span class="c6"></span></p><a id="id.2fzhg8bkhmss"></a>
    <h3 class="c27 c16" id="h.hvbcmqwzo9do"><span class="c10">NIST SP 800-53: AC-6</span></h3>
    <p class="c36 c16"><span>NIST developed SP 800-53</span><span>&nbsp;to provide businesses with </span><span
            class="c12">a </span><span>customizable</span><span class="c12">&nbsp;</span><span class="c6">information
            privacy plan. It's a comprehensive resource that describes a wide range of control categories. Each control
            provides a few key pieces of information:</span></p>
    <ul class="c26 lst-kix_u2raiarzwx9x-0 start">
        <li class="c22 li-bullet-0"><span class="c37">Control:</span><span class="c6">&nbsp;A definition of the security
                control.</span></li>
        <li class="c22 li-bullet-0"><span class="c37">Discussion:</span><span class="c6">&nbsp;A description of how the
                control should be implemented.</span></li>
        <li class="c22 li-bullet-0"><span class="c37">Control enhancements:</span><span class="c6">&nbsp;A list of
                suggestions to improve the effectiveness of the control.</span></li>
    </ul>
    <p class="c0"><span class="c6"></span></p>
    <table class="c2">
        <tbody>
            <tr class="c17">
                <td class="c23" colspan="1" rowspan="4">
                    <p class="c28"><span class="c5">AC-6</span></p>
                </td>
                <td class="c13" colspan="1" rowspan="1">
                    <p class="c3"><span class="c21">Least Privilege</span></p>
                </td>
            </tr>
            <tr class="c17">
                <td class="c13" colspan="1" rowspan="1">
                    <p class="c3"><span class="c12">Control:</span></p>
                    <p class="c3"><span class="c12">Only </span><span>the minimal access and authorization required to
                            complete a task or function should be provided to users.</span></p>
                </td>
            </tr>
            <tr class="c17">
                <td class="c13" colspan="1" rowspan="1">
                    <p class="c3"><span class="c6">Discussion:</span></p>
                    <p class="c3"><span>Processes, user accounts, and roles should be enforced as necessary to achieve
                            least privilege. </span><span>The intention is to prevent a user from operating at privilege
                            levels higher than what is necessary to accomplish business objectives.</span></p>
                </td>
            </tr>
            <tr class="c17">
                <td class="c13" colspan="1" rowspan="1">
                    <p class="c3"><span class="c6">Control enhancements:</span></p>
                    <ul class="c26 lst-kix_1uw4g06zww1z-0 start">
                        <li class="c22 li-bullet-0"><span class="c6">Restrict access to sensitive resources based on
                                user role.</span></li>
                        <li class="c22 li-bullet-0"><span class="c6">Automatically revoke access to information after a
                                period of time.</span></li>
                        <li class="c22 li-bullet-0"><span class="c6">Keep activity logs of provisioned user
                                accounts.</span></li>
                        <li class="c22 li-bullet-0"><span>Regularly audit user privileges.</span></li>
                    </ul>
                </td>
            </tr>
        </tbody>
    </table>
    <p class="c0"><span class="c6"></span></p>
    <p class="c16 c36"><span class="c37">Note:</span><span class="c6">&nbsp;In the category of access controls, SP
            800-53 lists least privilege sixth, i.e. AC-6.</span></p>
    <div>
        <hr>
        <p class="c16 c34"><span class="c6"></span></p>
        <p class="c34 c16"><span class="c6"></span></p>
    </div>
</body>
