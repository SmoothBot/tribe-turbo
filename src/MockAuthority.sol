// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity >=0.8.0;

import {Authority} from "./Auth.sol";
// @todo - make this an ownership based auth kinda thing.
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