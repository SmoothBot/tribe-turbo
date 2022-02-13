// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity >=0.8.0;

import {Auth, Authority} from "solmate/auth/Auth.sol";

contract MockAuthority is Authority {
    address immutable owner;

    constructor(address _owner) {
        owner = _owner;
    }

    function canCall(
        address user,
        address,
        bytes4
    ) public view override returns (bool) {
        return user == owner;
    }
}