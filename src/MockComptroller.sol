// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity 0.8.10;

import {ERC20} from "solmate/tokens/ERC20.sol";

import {CERC20} from "libcompound/interfaces/CERC20.sol";
import {Comptroller} from "./interfaces/Comptroller.sol";
import {FuseAdmin} from "./interfaces/FuseAdmin.sol";

/// @title Comptroller
/// @author Compound Labs and Rari Capital
/// @notice Minimal Compound/Fuse Comptroller interface.
contract MockComptroller is Comptroller, FuseAdmin {
    /// @notice Maps underlying tokens to their equivalent cTokens in a pool.
    /// @param token The underlying token to find the equivalent cToken for.
    /// @return The equivalent cToken for the given underlying token.
    function cTokensByUnderlying(ERC20 token) external view returns (CERC20) {
        return CERC20(address(token));
    }

    /// @notice Retrieves the admin of the Comptroller.
    /// @return The current administrator of the Comptroller.
    function admin() external view returns (address) {
        return address(this);
    }

    /// @notice Enters into a list of cToken markets, enabling them as collateral.
    /// @param cTokens The list of cTokens to enter into, enabling them as collateral.
    /// @return A list of error codes, or 0 if there were no failures in entering the cTokens.
    function enterMarkets(CERC20[] calldata cTokens) external returns (uint256[] memory) {
        return new uint256[](cTokens.length);
    }

    function _setWhitelistStatuses(address[] calldata users, bool[] calldata enabled) external { }
}
